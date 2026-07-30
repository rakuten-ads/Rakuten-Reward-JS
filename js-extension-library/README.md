# `Rakuten Mission SDK - JS Extension Library`

[![Language](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

The Rakuten Reward JS Extension Library is designed to bridge web pages loaded within native mobile app WebViews with native APIs. This allows web-based interfaces to interact directly with native functionalities, such as logging actions or triggering native events from web page elements.

Table of Contents

- [Installation](#installations)
- [API Methods](#api-methods)
  - [Set Platform](#set-platform)
  - [Log Action](#log-action)
  - [Open SDK Portal](#open-sdk-portal)
  - [Open SPS Portal](#open-sps-portal)
  - [Get Mission List (Lite)](#get-mission-list-lite)
  - [Get Mission Details](#get-mission-details)
  - [Get Unclaim List](#get-unclaim-list)
  - [Claim Mission Point](#claim-mission-point)
  - [Get User Points History](#get-user-points-history)
  - [Get User Reward Points](#get-user-reward-points)
  - [Get LinkShare Point History](#get-linkshare-point-history)
  - [Get LinkShare Processing Point](#get-linkshare-processing-point)
- [Types](#types)
  - [SDKResult](#sdkresult)
  - [ActionResult](#actionresult)
  - [MissionLite](#missionlite)
  - [MissionDetails](#missiondetails)
  - [UnclaimItem](#unclaimitem)
  - [PointHistoryItem](#pointhistoryitem)
  - [RewardRedeemRequest](#rewardredeemrequest)
  - [LSPointHistory](#lspointhistory)
  - [LSPointHistoryItem](#lspointhistoryitem)
- [Error Handling](#error-handling)
- [CHANGELOG](./CHANGELOG)

<br />

# `Installations`

## `Import file via script tag`

To install via script, import our JS SDK file by pasting the following `<script>` tag inside the `<header>` tag.

Source file: `https://portal.reward.rakuten.co.jp/sdk-static/jsext/{{VERSION}}/missionsdk-ext.js`<br />

Latest version: `https://portal.reward.rakuten.co.jp/sdk-static/jsext/1.3.0/missionsdk-ext.js`

```html
<header>
  // ... put this before the end of header tag
  <script
    type="text/javascript"
    src="https://portal.reward.rakuten.co.jp/sdk-static/jsext/1.3.0/missionsdk-ext.js"
  ></script>
</header>
```

After pasting the script, the SDK will be available via the `window.RakutenRewardExt` global.

```html
<script>
  const rewardSDKExt = window.RakutenRewardExt || {};
</script>
```

## `Setting platform`

Before using any API method, set the OS platform to `android` or `ios` to match the native host.

```html
<script>
  // Android WebView
  rewardSDKExt.setPlatform('android');

  // iOS WKWebView
  rewardSDKExt.setPlatform('ios');
</script>
```

<br />

# `API Methods`

## `Set Platform`

```javascript
rewardSDKExt.setPlatform('android' | 'ios')
```

| Parameter | Type                       | Required | Description                                    |
| --------- | -------------------------- | -------- | ---------------------------------------------- |
| platform  | `"android"` \| `"ios"`     | Yes      | Set the platform before calling any native API |

---

## `Log Action`

Logs a mission action. Supports an optional callback to receive the result. Omitting `callback` retains the original fire-and-forget behaviour.

```javascript
// Fire-and-forget (original behaviour — unchanged)
rewardSDKExt.logAction('daily_login');

// With result callback
rewardSDKExt.logAction('daily_login', (result) => {
  if (result.success) {
    console.log('Action logged successfully');
  } else {
    console.error('Failed:', result.error);
  }
});
```

| Parameter  | Type                                                          | Required | Description                    |
| ---------- | ------------------------------------------------------------- | -------- | ------------------------------ |
| actionCode | `string`                                                      | Yes      | Mission action code to log     |
| callback   | `(result:` [`ActionResult`](#actionresult)`) => void`         | No       | Receives the result of the action |

---

## `Open SDK Portal`

Opens the Reward SDK portal UI. Supports an optional callback to receive the result. Omitting `callback` retains the original fire-and-forget behaviour.

```javascript
// Fire-and-forget (original behaviour — unchanged)
rewardSDKExt.openSdkPortal();

// With result callback
rewardSDKExt.openSdkPortal((result) => {
  if (result.success) {
    console.log('Portal opened');
  } else {
    console.error('Failed:', result.error);
  }
});
```

| Parameter | Type                                                          | Required | Description                       |
| --------- | ------------------------------------------------------------- | -------- | --------------------------------- |
| callback  | `(result:` [`ActionResult`](#actionresult)`) => void`         | No       | Receives the result of the action |

---

## `Open SPS Portal`

Opens the Super Point Screen (SPS) portal. Supports an optional callback to receive the result. Omitting `callback` retains the original fire-and-forget behaviour.

```javascript
// Fire-and-forget (original behaviour — unchanged)
rewardSDKExt.openSpsPortal();

// With result callback
rewardSDKExt.openSpsPortal((result) => {
  if (result.success) {
    console.log('SPS portal opened');
  } else {
    console.error('Failed:', result.error);
  }
});
```

| Parameter | Type                                                          | Required | Description                       |
| --------- | ------------------------------------------------------------- | -------- | --------------------------------- |
| callback  | `(result:` [`ActionResult`](#actionresult)`) => void`         | No       | Receives the result of the action |

---

## `Get Mission List (Lite)`

Fetches the lite mission list. The lite version contains essential fields only and excludes progress. Returns `[]` on failure.

```javascript
rewardSDKExt.getMissionLite((missions) => {
  missions.forEach((m) => {
    console.log(m.name, m.actionCode, m.point + 'pt');
  });
});
```

| Parameter | Type                                                                                          | Required | Description                   |
| --------- | --------------------------------------------------------------------------------------------- | -------- | ----------------------------- |
| callback  | `(result:` [`SDKResult`](#sdkresult)`<`[`MissionLite`](#missionlite)`[]>) => void`            | No       | Receives the lite mission list wrapped in an `SDKResult` |

---

## `Get Mission Details`

Fetches full details for a single mission by action code, including progress. Returns `null` on failure or if `actionCode` is empty.

```javascript
rewardSDKExt.getMissionDetails('daily_login', (mission) => {
  if (!mission) {
    console.error('Mission not found');
    return;
  }
  console.log(mission.name, mission.progress + '/' + mission.times, mission.point + 'pt');
});
```

| Parameter  | Type                                                                                           | Required | Description                       |
| ---------- | ---------------------------------------------------------------------------------------------- | -------- | --------------------------------- |
| actionCode | `string`                                                                                       | Yes      | Action code of the mission to fetch |
| callback   | `(result:` [`SDKResult`](#sdkresult)`<`[`MissionDetails`](#missiondetails)`>) => void`         | No       | Receives the mission detail wrapped in an `SDKResult` |

---

## `Get Unclaim List`

Fetches the list of mission achievements that have been completed but whose points have not yet been claimed. Returns `[]` on failure.

```javascript
rewardSDKExt.getUnclaimList((items) => {
  items.forEach((item) => {
    console.log(item.name, item.point + 'pt unclaimed');
  });
});
```

| Parameter | Type                                                                                          | Required | Description                    |
| --------- | --------------------------------------------------------------------------------------------- | -------- | ------------------------------ |
| callback  | `(result:` [`SDKResult`](#sdkresult)`<`[`UnclaimItem`](#unclaimitem)`[]>) => void`            | No       | Receives the unclaimed items list wrapped in an `SDKResult` |

---

## `Claim Mission Point`

Claims the point for a completed mission achievement. The native claim UI (banner or modal) is displayed on success. Supports an optional callback — omitting it retains fire-and-forget behaviour.

Use `actionCode` and `achieveddatestr` from a [`getUnclaimList`](#get-unclaim-list) item.

```javascript
// Fire-and-forget (original behaviour — unchanged)
rewardSDKExt.claimMissionPoint('daily_login', '20260617');

// With result callback
rewardSDKExt.claimMissionPoint('daily_login', '20260617', (result) => {
  if (result.success) {
    console.log('Points claimed');
  } else {
    console.error('Failed:', result.error);
  }
});
```

| Parameter    | Type                                                          | Required | Description                                                          |
| ------------ | ------------------------------------------------------------- | -------- | -------------------------------------------------------------------- |
| actionCode   | `string`                                                      | Yes      | Action code from the unclaim item                                    |
| achievedDate | `string`                                                      | Yes      | Achievement date in `yyyyMMdd` format (from `achieveddatestr`)       |
| callback     | `(result:` [`ActionResult`](#actionresult)`) => void`         | No       | Receives the result of the claim action                              |

---

## `Get User Points History`

```javascript
rewardSDKExt.getPointHistory((result) => {
  if (result.success) {
    console.log('Points History:', result.data); // [{ points: 1, month: '202504' }, ...]
  }
});
```

| Parameter | Type                                                                                           | Required | Description               |
| --------- | ---------------------------------------------------------------------------------------------- | -------- | ------------------------- |
| callback  | `(result:` [`SDKResult`](#sdkresult)`<`[`PointHistoryItem`](#pointhistoryitem)`[]>) => void`   | No       | Receives the point history wrapped in an `SDKResult` |

---

## `Get User Reward Points`

```javascript
rewardSDKExt.getUserRewardPoint((result) => {
  if (result.success) {
    console.log('Reward Points:', result.data); // 10
  }
});
```

| Parameter | Type                                                                    | Required | Description                          |
| --------- | ----------------------------------------------------------------------- | -------- | ------------------------------------ |
| callback  | `(result:` [`SDKResult`](#sdkresult)`<number>) => void`                 | No       | Receives the reward points wrapped in an `SDKResult` |

---

## `Get LinkShare Point History`

Returns paginated point history for a LinkShare tenant.

```javascript
const requestData = {
  tenantId: 'your-tenant-id',
  appName: 'your-app-name',
};
rewardSDKExt.getLSPointHistory(requestData, 0, 20, (history) => {
  console.log('LinkShare Point History:', history);
  // {
  //   "total": 2,
  //   "offset": 0,
  //   "limit": 20,
  //   "history": [{ "point": 150, "advertiser": "Rakuten Fashion", ... }]
  // }
});
```

| Parameter   | Type                                                                                         | Required | Description                      |
| ----------- | -------------------------------------------------------------------------------------------- | -------- | -------------------------------- |
| requestData | [`RewardRedeemRequest`](#rewardredeemrequest)                                                 | Yes      | Tenant ID and application name   |
| offset      | `number`                                                                                     | Yes      | Pagination offset                |
| limit       | `number`                                                                                     | Yes      | Number of items to return        |
| callback    | `(result:` [`SDKResult`](#sdkresult)`<`[`LSPointHistory`](#lspointhistory)`>) => void`       | No       | Receives the paginated history wrapped in an `SDKResult` |

---

## `Get LinkShare Processing Point`

Returns `-1` on failure.

```javascript
const requestData = {
  tenantId: 'your-tenant-id',
  appName: 'your-app-name',
};
rewardSDKExt.getLSProcessingPoint(requestData, (points) => {
  console.log('LinkShare Processing Points:', points); // 28
});
```

| Parameter   | Type                                                                        | Required | Description                         |
| ----------- | --------------------------------------------------------------------------- | -------- | ----------------------------------- |
| requestData | [`RewardRedeemRequest`](#rewardredeemrequest)                                | Yes      | Tenant ID and application name      |
| callback    | `(result:` [`SDKResult`](#sdkresult)`<number>) => void`                     | No       | Receives the processing point total wrapped in an `SDKResult` |

---

## `Error Handling`

All SDK methods return a `Promise`. Errors — such as missing platform, invalid app key, or no native SDK present — are thrown asynchronously, so a plain `try/catch` block **will not catch them**. You must either `await` the call or use `.catch()`.

### Using async/await

```javascript
async function openPortal() {
  try {
    await rewardSDKExt.openSpsPortal((result) => {
      if (result.success) {
        console.log('SPS portal opened successfully');
      } else {
        console.warn('SDK returned failure:', result.error);
      }
    });
  } catch (error) {
    // thrown when platform is not set, app key is missing, etc.
    console.error('SDK error:', error);
  }
}
```

### Using Promise .catch()

```javascript
rewardSDKExt.openSpsPortal((result) => {
  if (result.success) {
    console.log('SPS portal opened successfully');
  } else {
    console.warn('SDK returned failure:', result.error);
  }
}).catch((error) => {
  console.error('SDK error:', error);
});
```

> **Note:** `result.success === false` inside the callback means the native SDK completed the call but reported a failure (e.g. `sdk_not_active`, `user_not_consent`). A thrown error caught by `catch` means the call never reached the native SDK at all (e.g. platform not set, invalid app key).

### Why plain try/catch does not work

```javascript
// ❌ This will NOT catch SDK errors
try {
  rewardSDKExt.openSpsPortal(callback); // returns a Promise — errors go unhandled
} catch (error) {
  // never runs
}

// ✓ Await the Promise so the rejection becomes catchable
try {
  await rewardSDKExt.openSpsPortal(callback);
} catch (error) {
  // runs correctly
}
```

This applies to every SDK method: `logAction`, `openSdkPortal`, `openSpsPortal`, `claimMissionPoint`, `getMissionLite`, `getMissionDetails`, `getUnclaimList`, `getUserRewardPoint`, `getPointHistory`, `getLSPointHistory`, and `getLSProcessingPoint`.

---

<br />

# `Types`

## `SDKResult`

The unified result shape returned by all callback-based APIs.

| Key           | Type      | Description                                               |
| ------------- | --------- | --------------------------------------------------------- |
| success       | `boolean` | `true` if the operation completed successfully            |
| data          | `T`       | The returned payload — present on success for data APIs   |
| error         | `string`  | Only present on failure — see error codes under [`ActionResult`](#actionresult) |
| consentStatus | `string`  | Present when `error` is `user_not_consent`                |

---

## `ActionResult`

Type alias for `SDKResult` (no data payload). Returned by [`logAction`](#log-action), [`openSdkPortal`](#open-sdk-portal), [`openSpsPortal`](#open-sps-portal), and [`claimMissionPoint`](#claim-mission-point) when a callback is provided.

**Error codes** (applies to all APIs via `SDKResult.error`)

| Error code           | Description                                   |
| -------------------- | --------------------------------------------- |
| `invalid_appkey`     | The app key provided does not match           |
| `sdk_not_active`     | SDK session not started (user not logged in)  |
| `user_not_consent`   | User has not accepted Reward Terms of Service |
| `network_error`      | Network connection error                      |
| `invalid_request`    | Invalid parameter or action code              |
| `mission_reach_cap`  | Mission has reached its daily achievement cap |
| `unknown`            | Unexpected error                              |

---

## `MissionLite`

Returned by [`getMissionLite`](#get-mission-list-lite).

| Key              | Type              | Description                                        |
| ---------------- | ----------------- | -------------------------------------------------- |
| name             | `string \| null`  | Mission name                                       |
| actionCode       | `string \| null`  | Action code — pass to [`logAction`](#log-action)   |
| iconurl          | `string \| null`  | Mission icon URL                                   |
| instruction      | `string \| null`  | Mission instruction text                           |
| condition        | `string \| null`  | Mission completion condition                       |
| notificationtype | `string \| null`  | One of: `NONE`, `BANNER`, `MODAL`, `CUSTOM`        |
| point            | `number`          | Points awarded on completion                       |
| enddatestr       | `string \| null`  | Mission end date in `yyyyMMdd` format              |
| till             | `string \| null`  | Human-readable days remaining, e.g. `"残り3日"`   |
| additional       | `string \| null`  | Additional message                                 |
| times            | `number`          | Number of required actions to complete the mission |

---

## `MissionDetails`

Returned by [`getMissionDetails`](#get-mission-details). Extends [`MissionLite`](#missionlite) with the following additional fields:

| Key        | Type      | Description                                        |
| ---------- | --------- | -------------------------------------------------- |
| reachedCap | `boolean` | Whether the daily achievement cap has been reached |
| progress   | `number`  | Current action progress toward completion          |

---

## `UnclaimItem`

Returned by [`getUnclaimList`](#get-unclaim-list).

| Key              | Type               | Description                                                                                  |
| ---------------- | ------------------ | -------------------------------------------------------------------------------------------- |
| name             | `string \| null`   | Mission name                                                                                 |
| iconurl          | `string \| null`   | Mission icon URL                                                                             |
| instruction      | `string \| null`   | Mission instruction text                                                                     |
| actionCode       | `string \| null`   | Action code — pass to [`claimMissionPoint`](#claim-mission-point)                            |
| custom           | `boolean`          | Whether the claim notification is a custom notification                                      |
| notificationtype | `string \| null`   | One of: `NONE`, `BANNER`, `MODAL`, `CUSTOM`                                                  |
| point            | `number \| null`   | Points to be claimed                                                                         |
| unclaimed        | `number \| null`   | Number of unclaimed items                                                                    |
| achieveddatestr  | `string \| null`   | Achievement date in `yyyyMMdd` format — pass to [`claimMissionPoint`](#claim-mission-point)  |

---

## `PointHistoryItem`

Each element in the `data` array returned by [`getPointHistory`](#get-user-points-history).

| Key    | Type     | Description                         | Example    |
| ------ | -------- | ----------------------------------- | ---------- |
| points | `number` | Points earned in the specific month | `1`        |
| month  | `string` | Month of the points earned          | `'202504'` |

---

## `RewardRedeemRequest`

Used by [`getLSPointHistory`](#get-linkshare-point-history) and [`getLSProcessingPoint`](#get-linkshare-processing-point).

| Key      | Type     | Description      |
| -------- | -------- | ---------------- |
| tenantId | `string` | Tenant ID        |
| appName  | `string` | Application name |

---

## `LSPointHistory`

Returned by [`getLSPointHistory`](#get-linkshare-point-history).

| Key     | Type                                                              | Description                   |
| ------- | ----------------------------------------------------------------- | ----------------------------- |
| total   | `number`                                                          | Total number of history items |
| offset  | `number`                                                          | Current offset for pagination |
| limit   | `number`                                                          | Number of items per page      |
| history | [`LSPointHistoryItem`](#lspointhistoryitem)`[]`                   | Array of point history items  |

---

## `LSPointHistoryItem`

| Key             | Type      | Description                                |
| --------------- | --------- | ------------------------------------------ |
| point           | `number`  | Points earned                              |
| advertiser      | `string`  | Name of the advertiser                     |
| grantDate       | `string`  | Date when points were granted (YYYY-MM-DD) |
| transactionDate | `string`  | Date of the transaction (YYYY-MM-DD)       |
| orderId         | `string`  | Order ID                                   |
| tncUrl          | `string`  | Terms and conditions URL                   |
| isPointGranted  | `boolean` | Whether points have been granted           |
