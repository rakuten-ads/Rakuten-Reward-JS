# 楽天ミッションSDK - JS拡張ライブラリ

[![Language](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

楽天リワードJS拡張ライブラリは、ネイティブモバイルアプリのWebView内で読み込まれるウェブページとネイティブAPIを橋渡しするために設計されています。これにより、ウェブベースのインターフェースがネイティブの機能と直接対話できるようになります。


コンテンツ

- [インストール](#インストール)
- [APIメソッド ](#apiメソッド) 
- [CHANGELOG](../../CHANGELOG.md)


<br />

# インストール

## スクリプトタグを介してファイルをインポート

スクリプトを介してインストールするには、以下の`<script>`タグを`<header>`タグ内に貼り付けて、JS SDKファイルをインポートします。

ソースファイル: `https://portal.reward.rakuten.co.jp/sdk-static/jsext/{{VERSION}}/missionsdk-ext.js`<br />

最新バージョン: `https://portal.reward.rakuten.co.jp/sdk-static/jsext/0.0.1/missionsdk-ext.js`

```html
<header>
  // ... ヘッダータグの終了前にこれを配置
  <script
    type="text/javascript"
    src="https://portal.reward.rakuten.co.jp/sdk-static/jsext/0.0.1/missionsdk-ext.js"
  ></script>
</header>
```
スクリプトを貼り付けた後、Mission SDK JSは利用可能になり、RakutenRewardExt 変数を通じてウィンドウオブジェクト内でアクセスできます。  

```html
<script>
  const rewardSDKExt = window.RakutenRewardExt || {};
</script>
```

## プラットフォームの設定
APIメソッドを使用する前に、OSプラットフォーム `Android` または `iOS` を適切に設定する必要があります。  

```html
<script>
    // Androidプラットフォームの設定
    rewardSDKExt.setPlatform("android");
    
    // iOSプラットフォームの設定
    rewardSDKExt.setPlatform("ios");
</script>
```

# APIメソッド  

## プラットフォームの設定  

```javascript
rewardSDKExt.setPlatform(platform: "android" | "ios"): void
```

| 関数  | 非同期 | パラメータ | レスポンスタイプ | 説明 |
| --- | --- | --- | --- | --- |
| logAction | はい   | (platform: "android" \| "ios") | | ネイティブAPIをトリガーする前にプラットフォームを設定 |

## アクションを送信する

```javascript
rewardSDKExt.logAction(actionCode: string): void
```

| 関数  | 非同期 | パラメータ | レスポンスタイプ | 説明 |
| --- | --- | --- | --- | --- |
| logAction | はい   | (actionCode: string) | | アクションログのネイティブAPIをトリガー |

## SDKポータルを開く

```javascript
rewardSDKExt.openSdkPortal(): void
```

| 関数  | 非同期 | パラメータ | レスポンスタイプ | 説明 |
| --- | --- | --- | --- | --- |
| openSdkPortal | はい   |  | | SDKポータルを開くネイティブAPIをトリガー |

## SPSポータルを開く

```javascript
rewardSDKExt.openSpsPortal(): void
```

| 関数  | 非同期 | パラメータ | レスポンスタイプ | 説明 |
| --- | --- | --- | --- | --- |
| openSpsPortal | はい   | | | SPSポータルを開くネイティブAPIをトリガー |
  
---
言語 :
> [![en](../../assets/lang/en.png)](../README.md)