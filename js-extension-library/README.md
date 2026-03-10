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

Latest version: `https://portal.reward.rakuten.co.jp/sdk-static/jsext/1.2.0/missionsdk-ext.js`

```html
<header>
  // ... put this before the end of header tag
  <script
    type="text/javascript"
    src="https://portal.reward.rakuten.co.jp/sdk-static/jsext/1.2.0/missionsdk-ext.js"
  ></script>
</header>
```

After pasting the script, Mission SDK JS will be available and can be accessed in the window object, through the RewardMissionSDK variable.

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
  rewardSDKExt.setPlatform('android');

  // Setting iOS Platform
  rewardSDKExt.setPlatform('ios');
</script>
```

# `API Methods`

## `Set Platform`

```javascript
rewardSDKExt.setPlatform(platform: "android" | "ios"): void
```

| function  | async | parameters                     | response type | description                                       |
| --------- | ----- | ------------------------------ | ------------- | ------------------------------------------------- |
| logAction | yes   | (platform: "android" \| "ios") |               | Set the platform before triggering the native API |

## `Log Action`

```javascript
rewardSDKExt.logAction(actionCode: string): void
```

| function  | async | parameters           | response type | description                    |
| --------- | ----- | -------------------- | ------------- | ------------------------------ |
| logAction | yes   | (actionCode: string) |               | Triggers log action native API |

## `Open SDK Portal`

```javascript
rewardSDKExt.openSdkPortal(): void
```

| function  | async | parameters | response type | description                            |
| --------- | ----- | ---------- | ------------- | -------------------------------------- |
| logAction | yes   |            |               | Triggers native API to open SDK Portal |

## `Open SPS Portal`

```javascript
rewardSDKExt.openSpsPortal(): void
```

| function  | async | parameters | response type | description                            |
| --------- | ----- | ---------- | ------------- | -------------------------------------- |
| logAction | yes   |            |               | Triggers native API to open SPS Portal |

## `Get User Points History`

```javascript
rewardSDKExt.getPointHistory((point: unknown) => {
  console.log('Points History:', point); // [{ points: 1, month: '202504' }, ...]
});
```

| function        | async | parameters                 | response type | description              |
| --------------- | ----- | -------------------------- | ------------- | ------------------------ |
| getPointHistory | yes   | callback<`PointHistory`[]> | void          | Get users points history |

### `PointHistory`

| Key    | Type    | Mandatory | Default Value | Description                         | Example Value |
| ------ | ------- | --------- | ------------- | ----------------------------------- | ------------- |
| points | Integer | Yes       | 0             | Points earned in the specific month | 1             |
| month  | String  | Yes       | ''            | Month of the points earned          | '202504'      |

## `Get User Reward Points`

```javascript
rewardSDKExt.getUserRewardPoint((points: number) => {
  console.log('Reward Points:', points); // 10
});
```

| function           | async | parameters       | response type | description             |
| ------------------ | ----- | ---------------- | ------------- | ----------------------- |
| getUserRewardPoint | yes   | callback<number> | void          | Get users reward points |

## `Get LinkShare Point History`

```javascript
const requestData = {
  tenantId: 'your-tenant-id',
  appName: 'your-app-name'
};
rewardSDKExt.getLSPointHistory(requestData, 0, 20, (history) => {
  console.log('LinkShare Point History:', history);
  // {
  //   "total": 2,
  //   "offset": 0,
  //   "limit": 20,
  //   "history": [
  //     {
  //       "point": 150,
  //       "advertiser": "Rakuten Fashion",
  //       "grantDate": "2025-12-10",
  //       "transactionDate": "2025-12-05",
  //       "orderId": "ORDER-2025-001234",
  //       "tncUrl": "https://example.com/terms-and-conditions",
  //       "isPointGranted": true
  //     }
  //   ]
  // }
});
```

| function           | async | parameters                                                         | response type | description                          |
| ------------------ | ----- | ------------------------------------------------------------------ | ------------- | ------------------------------------ |
| getLSPointHistory  | yes   | (requestData: RewardRedeemRequest, offset: number, limit: number, callback\<LSPointHistory\>) | void          | Get LinkShare point history with pagination |

### `RewardRedeemRequest`

| Key      | Type   | Description                                    |
| -------- | ------ | ---------------------------------------------- |
| tenantId | String | Tenant ID                                      |
| appName  | String | Application name                               |

### `LSPointHistory`

| Key     | Type                   | Description                                    |
| ------- | ---------------------- | ---------------------------------------------- |
| total   | Integer                | Total number of history items                  |
| offset  | Integer                | Current offset for pagination                  |
| limit   | Integer                | Number of items per page                       |
| history | `LSPointHistoryItem[]` | Array of point history items                   |

### `LSPointHistoryItem`

| Key             | Type    | Description                                    |
| --------------- | ------- | ---------------------------------------------- |
| point           | Integer | Points earned                                  |
| advertiser      | String  | Name of the advertiser                         |
| grantDate       | String  | Date when points were granted (YYYY-MM-DD)     |
| transactionDate | String  | Date of the transaction (YYYY-MM-DD)           |
| orderId         | String  | Order ID                                       |
| tncUrl          | String  | Terms and conditions URL                       |
| isPointGranted  | Boolean | Whether points have been granted               |

## `Get LinkShare Processing Point`

```javascript
const requestData = {
  tenantId: 'your-tenant-id',
  appName: 'your-app-name'
};
rewardSDKExt.getLSProcessingPoint(requestData, (points) => {
  console.log('LinkShare Processing Points:', points); // 28
});
```

| function              | async | parameters                                        | response type | description                       |
| --------------------- | ----- | ------------------------------------------------- | ------------- | --------------------------------- |
| getLSProcessingPoint  | yes   | (requestData: RewardRedeemRequest, callback\<number\>) | void          | Get LinkShare processing points   |
