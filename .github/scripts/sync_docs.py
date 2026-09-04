import os
import re
import subprocess
import sys
from openai import OpenAI

PAGES_REPO_DIR = os.environ["PAGES_REPO_DIR"]
AI_API_KEY = os.environ["RAKUTEN_AI_API_KEY"]
AI_MODEL = os.environ["RAKUTEN_AI_MODEL"]
CONFLUENCE_PAT = os.environ.get("CONFLUENCE_PAT", "")
CONFLUENCE_BASE_URL = "https://confluence.rakuten-it.com/confluence"
CONFLUENCE_REPORT_PARENT_ID = "6893456549"

client = OpenAI(
    api_key=AI_API_KEY,
    base_url="https://api.ai.public.rakuten-it.com/rakutenllms/v1/",
)

# Maps source file (relative to repo root) -> list of target paths (relative to pages repo root).
# JS has no separate JA source docs (except js-extension-library/ja), so English source updates
# both EN and JA targets — the AI adapts language to match TARGET.
MAPPING = {
    "README.md": [
        "docs/javascript/index.md",
        "docs/javascript/integration.md",
        "docs/javascript/authentication.md",
        "docs/javascript/mission.md",
        "docs/javascript/consent.md",
        "docs/javascript/ui.md",
        "docs/ja/javascript/index.md",
        "docs/ja/javascript/integration.md",
        "docs/ja/javascript/authentication.md",
        "docs/ja/javascript/mission.md",
        "docs/ja/javascript/consent.md",
        "docs/ja/javascript/ui.md",
    ],
    "API.md": [
        "docs/javascript/api-reference.md",
        "docs/ja/javascript/api-reference.md",
    ],
    "UI.md": [
        "docs/javascript/ui.md",
        "docs/javascript/authentication.md",
        "docs/javascript/consent.md",
        "docs/ja/javascript/ui.md",
        "docs/ja/javascript/authentication.md",
        "docs/ja/javascript/consent.md",
    ],
    "FAQ.md": [
        "docs/javascript/faq.md",
        "docs/ja/javascript/faq.md",
    ],
    "js-extension-library/README.md": [
        "docs/javascript/js-extension.md",
        "docs/ja/javascript/js-extension.md",
    ],
    "js-extension-library/ja/README.md": [
        "docs/ja/javascript/js-extension.md",
    ],
}

# Maps source file -> list of Confluence JavaScript page dicts {id, title}
CONFLUENCE_MAPPING = {
    "README.md": [
        {"id": "6863539184", "title": "3 - Setup | 🌐 JavaScript"},
        {"id": "6863539188", "title": "4 - Initialization | 🌐 JavaScript"},
        {"id": "6863539192", "title": "5 - Authentication | 🌐 JavaScript"},
        {"id": "6863539200", "title": "6 - Missions and Points | 🌐 JavaScript"},
        {"id": "6863539208", "title": "7 - Consent | 🌐 JavaScript"},
        {"id": "6863539233", "title": "8 - Portal UI | 🌐 JavaScript"},
    ],
    "UI.md": [
        {"id": "6863539208", "title": "7 - Consent | 🌐 JavaScript"},
        {"id": "6863539233", "title": "8 - Portal UI | 🌐 JavaScript"},
    ],
    "API.md": [
        {"id": "6863539170", "title": "11 - Configuration | 🌐 JavaScript"},
        {"id": "6863539174", "title": "12 - API Data | 🌐 JavaScript"},
        {"id": "6863539178", "title": "13 - API Reference | 🌐 JavaScript"},
    ],
    "js-extension-library/README.md": [
        {"id": "6863539159", "title": "10 - JavaScript Extension | 🌐 JavaScript"},
    ],
    "FAQ.md": [
        {"id": "6897972016", "title": "14 - FAQ | 🌐 JavaScript"},
    ],
}

SYSTEM_PROMPT = """You are a technical documentation editor for the Rakuten Reward JavaScript SDK.

You will receive:
- DIFF: a git diff showing exactly what changed in a source documentation file from the SDK repository
- TARGET: the corresponding public-facing documentation page on the GitHub Pages site

Your task:
1. Read the DIFF carefully — lines starting with + were added, lines starting with - were removed.
2. Apply only those specific changes to TARGET, adapting them to match TARGET's tone, formatting, and style.
3. Do not rewrite or restructure sections that were not touched by the diff.
4. If TARGET is written in Japanese, translate the changes into natural Japanese matching the tone of the surrounding page. If TARGET is written in English, keep the changes in English.
5. Skip any changes related to RID token, RAE token, or internal Rakuten authentication mechanisms — these are internal details that must not be disclosed publicly.
6. Return ONLY the complete updated TARGET file content with no explanation or commentary."""

CONFLUENCE_REVIEW_PROMPT = """You are a technical documentation editor for the Rakuten Reward JavaScript SDK.

INPUTS
- DIFF: a git diff (Markdown) showing what changed in a source documentation file in the SDK repo.
- CURRENT_PAGE: the CURRENT Confluence page content in Confluence storage XHTML format. This is the ONLY source of truth for the "Current" text you report.

GOAL
Produce a concise HTML review that lists what needs to be changed **on the Confluence page** so that its content stays consistent with the DIFF. This is a review to help a human editor manually edit the Confluence page — it is NOT a description of the source markdown diff.

METHOD (do this in order, silently)
1. Extract the semantic changes from the DIFF: what information was added, removed, or modified (e.g. a new API, a renamed property, a changed version number, a new step, a removed limitation). Ignore purely cosmetic Markdown-only edits (heading level tweaks, reflowed lines, link path changes, image path changes) that carry no semantic meaning for the reader.
2. For each semantic change, search CURRENT_PAGE (Confluence XHTML) to find where that topic is covered.
3. Decide per change:
   a. If CURRENT_PAGE already reflects the new state (e.g. it already mentions the new API, already shows the new version) → SKIP it, do not report.
   b. If CURRENT_PAGE covers the topic but with outdated wording/values → report it as a change item.
   c. If CURRENT_PAGE does not cover the topic at all but should → report it as an "Add" item with Current = <em>Not present</em>.
   d. If CURRENT_PAGE covers content that the DIFF removed and the removal is meaningful → report as a "Remove" item with Proposed = <em>Remove</em>.
4. If, after step 3, no items remain, output exactly: <p>No changes needed.</p>

OUTPUT FORMAT
- Return ONLY Confluence storage XHTML, no prose, no markdown, no code fences around the whole output.
- One <ul> containing one <li> per change item. Each <li> must have this exact structure:
  <li><p><strong>Section:</strong> heading or short locator inside the Confluence page (e.g. "Initialization" or "Table row: logAction")</p><p><strong>Current:</strong> exact wording copied from CURRENT_PAGE (or <em>Not present</em>)</p><p><strong>Proposed:</strong> the replacement wording, phrased in the same tone/format as the surrounding Confluence page</p></li>
- Keep <code>...</code> around inline code, method names, or values.
- Do NOT include raw markdown diff markers (+, -), do NOT quote lines from the diff, do NOT reference "the diff" in the output.
- Do NOT propose changes that only appear on GitHub Pages (e.g. VitePress-only syntax like `::: info`, relative links to `./debugging`, image paths under `/assets/…`). Confluence uses its own macros.
- Skip anything related to RID/RAE token content only if it is entirely internal boilerplate; otherwise include it — Confluence is internal so RID/RAE is allowed."""


def get_diff(source_path):
    base = None
    head = "HEAD"

    if os.environ.get("GITHUB_EVENT_NAME") == "push":
        try:
            import json
            with open(os.environ["GITHUB_EVENT_PATH"], encoding="utf-8") as f:
                payload = json.load(f)
            before = payload.get("before")
            # 40 zeros = new branch, no valid base to diff from
            if before and set(before) != {"0"}:
                base = before
                head = payload.get("after") or os.environ.get("GITHUB_SHA") or head
        except Exception:
            base = None

    cmd = (
        ["git", "diff", base, head, "--", source_path]
        if base
        else ["git", "diff", "HEAD~1", "HEAD", "--", source_path]
    )
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip()


def update_page(source_path, target_rel_path):
    target_abs_path = os.path.join(PAGES_REPO_DIR, target_rel_path)

    if not os.path.exists(target_abs_path):
        print(f"  SKIP: target not found: {target_abs_path}")
        return

    diff = get_diff(source_path)
    if not diff:
        print(f"  SKIP: no diff found for {source_path}")
        return

    target_content = open(target_abs_path, encoding="utf-8").read()

    response = client.chat.completions.create(
        model=AI_MODEL,
        temperature=0.0,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"DIFF:\n{diff}\n\nTARGET:\n{target_content}",
            },
        ],
    )

    updated = response.choices[0].message.content
    if not updated or not updated.strip():
        print(f"  WARN: empty AI response for {target_rel_path}; skipping write")
        return
    with open(target_abs_path, "w", encoding="utf-8") as f:
        f.write(updated)
    print(f"  updated: {target_rel_path}")


# --- Confluence review report ---

def get_latest_version():
    """Parse the latest JS SDK version from the top-level README.md script tag."""
    readme = open("README.md", encoding="utf-8").read()
    match = re.search(r'/sdk-static/sdk/(\d+\.\d+\.\d+)/missionsdk\.js', readme)
    return match.group(1) if match else "unknown"


def get_confluence_page(page_id):
    import requests
    url = f"{CONFLUENCE_BASE_URL}/rest/api/content/{page_id}?expand=body.storage,version,title"
    resp = requests.get(
        url,
        headers={"Authorization": f"Bearer {CONFLUENCE_PAT}", "Accept": "application/json"},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def build_confluence_review_section(source_path, page_info):
    diff = get_diff(source_path)
    if not diff:
        return None

    page_id = page_info["id"]
    page_title = page_info["title"]
    page_url = f"{CONFLUENCE_BASE_URL}/pages/viewpage.action?pageId={page_id}"

    try:
        page_data = get_confluence_page(page_id)
        current_html = page_data["body"]["storage"]["value"]
    except Exception as e:
        print(f"  WARN: could not fetch Confluence page {page_id}: {e}")
        return None

    response = client.chat.completions.create(
        model=AI_MODEL,
        temperature=0.0,
        messages=[
            {"role": "system", "content": CONFLUENCE_REVIEW_PROMPT},
            {"role": "user", "content": f"DIFF:\n{diff}\n\nCURRENT_PAGE:\n{current_html}"},
        ],
    )
    proposed = response.choices[0].message.content.strip()

    if "<p>No changes needed.</p>" in proposed:
        print(f"  no changes needed: {page_title}")
        return None

    print(f"  changes found: {page_title}")
    return f'<h2><a href="{page_url}">{page_title}</a></h2>\n{proposed}'


def create_confluence_report_page(version, sections_html):
    import requests
    title = f"JavaScript {version} Guide Update"
    body = (
        "<p>Proposed changes generated from the latest commit. "
        "Review each section below and apply the changes manually to the linked pages.</p>\n"
        + "\n<hr/>\n".join(sections_html)
    )
    payload = {
        "type": "page",
        "title": title,
        "ancestors": [{"id": CONFLUENCE_REPORT_PARENT_ID}],
        "space": {"key": "RADS"},
        "body": {
            "storage": {
                "value": body,
                "representation": "storage",
            }
        },
    }
    url = f"{CONFLUENCE_BASE_URL}/rest/api/content"
    resp = requests.post(
        url,
        json=payload,
        headers={
            "Authorization": f"Bearer {CONFLUENCE_PAT}",
            "Content-Type": "application/json",
        },
        timeout=30,
    )
    resp.raise_for_status()
    created = resp.json()
    page_url = f"{CONFLUENCE_BASE_URL}/pages/viewpage.action?pageId={created['id']}"
    print(f"  report page created: {page_url}")
    return page_url


def sync_confluence_review(changed_files):
    if not CONFLUENCE_PAT:
        print("CONFLUENCE_PAT not set — skipping Confluence review.")
        return

    if not CONFLUENCE_MAPPING:
        print("CONFLUENCE_MAPPING is empty — skipping Confluence review.")
        return

    print("\nGenerating Confluence review report...")
    version = get_latest_version()
    seen_pages = set()
    sections = []

    for source_file in changed_files:
        cf_pages = CONFLUENCE_MAPPING.get(source_file)
        if not cf_pages:
            continue
        for page_info in cf_pages:
            pid = page_info["id"]
            if pid in seen_pages:
                continue
            seen_pages.add(pid)
            print(f"  Analysing: {page_info['title']}")
            section = build_confluence_review_section(source_file, page_info)
            if section:
                sections.append(section)

    if sections:
        create_confluence_report_page(version, sections)
    else:
        print("  No Confluence changes needed.")


def main():
    changed_files = [f.strip() for f in sys.argv[1:] if f.strip()]
    if not changed_files:
        print("No changed files provided.")
        return

    # GitHub Pages sync
    seen_pairs = set()
    for source_file in changed_files:
        targets = MAPPING.get(source_file)
        if not targets:
            print(f"No mapping for: {source_file} — skipping")
            continue
        print(f"Processing: {source_file}")
        for target in targets:
            pair = (source_file, target)
            if pair in seen_pairs:
                print(f"  already updated from {source_file}: {target}")
                continue
            seen_pairs.add(pair)
            update_page(source_file, target)

    # Confluence review report
    sync_confluence_review(changed_files)


if __name__ == "__main__":
    main()
