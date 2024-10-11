# `Rakuten Mission SDK - JS Extension Library`

[![Language](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

The Rakuten Reward JS Extension Library is designed to bridge web pages loaded within native mobile app WebViews with native APIs. This allows web-based interfaces to interact directly with native functionalities, such as logging actions or triggering native events from web page elements.


Table of Contents

- [Installation](#installations)
- [API Methods](#api-methods) 
- [CHANGELOG](./CHANGELOG)


<br />

# `Installations`

## `Import file via script tag`

To install via script, import our JS SDK file by pasting the following `<script>` tag inside the `<header>` tag.

Source file: `https://portal.reward.rakuten.co.jp/sdk-static/jsext/{{VERSION}}/missionsdk-ext.js`<br />

Latest version: `https://portal.reward.rakuten.co.jp/sdk-static/jsext/0.0.1/missionsdk-ext.js`

```html
<header>
  // ... put this before the end of header tag
  <script
    type="text/javascript"
    src="https://portal.reward.rakuten.co.jp/sdk-static/jsext/0.0.1/missionsdk-ext.js"
  ></script>
</header>
```
After pasting the script, Mission SDK JS will be available and can be accessed in the window object, through the RakutenRewardExt variable.

```html
<script>
  const rewardSDKExt = window.RakutenRewardExt || {};
</script>
```

## `Setting platform`
Before we can use the API methods, we have to set the OS platform `Android` or `iOS` accordingly.

```html
<script>
    // Setting platform for Android
    rewardSDKExt.setPlatform("android");
    
    // Setting iOS Platform
    rewardSDKExt.setPlatform("ios");
</script>
```

# `API Methods`

## `Set Platform`


```javascript
rewardSDKExt.setPlatform(platform: "android" | "ios"): void
```

| function  | async | parameters                                                                                                     | response type                                               | description                                     |
| --------- | ----- | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------- |
| setPlatform | yes   | (platform: "android" \| "ios") | | Set the platform before triggering the native API |

## `Log Action`


```javascript
rewardSDKExt.logAction(actionCode: string): void
```

| function  | async | parameters                                                                                                     | response type                                               | description                                     |
| --------- | ----- | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------- |
| logAction | yes   | (actionCode: string) | | Triggers log action native API|

## `Open SDK Portal`


```javascript
rewardSDKExt.openSdkPortal(): void
```

| function  | async | parameters                                                                                                     | response type                                               | description                                     |
| --------- | ----- | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------- |
| openSdkPortal | yes   |  | | Triggers native API to open SDK Portal|

## `Open SPS Portal`


```javascript
rewardSDKExt.openSpsPortal(): void
```

| function  | async | parameters                                                                                                     | response type                                               | description                                     |
| --------- | ----- | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------- |
| openSpsPortal | yes   | | | Triggers native API to open SPS Portal|
  
---
Language :
> [![ja](../assets/lang/ja.png)](./ja/README.md)