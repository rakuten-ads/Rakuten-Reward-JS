# `API Reference`

Table of Contents

- [Initialization](#initialization)
- [Authentication](#authentication)
- [User](#user)
- [User Consent](#user-consent)
- [Mission](#mission)
- [Claim Points](#claim-points)
- [Points History](#points-history)
- [Mission SDK Portal](#mission-sdk-portal)
- [Other Pages](#other-pages)
- [Class Object](#class-object)
- [Error Code](#error-codes)

## `Initialization`

| Function | Async | Parameters                      | Response | Description            |
| -------- | ----- | ------------------------------- | -------- | ---------------------- |
| init     | No    | [SDKInitParams](#sdkinitparams) | Void     | Initialize Mission SDK |

## `Authentication`

### `Authentication Functions`

| Function            | Async | Parameters                                          | Response                                      | Description                                                                    |
| ------------------- | ----- | --------------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------ |
| getLoginUrl         | No    | No                                                  | String                                        | Returns Rakuten Login URL                                                      |
| openLoginUrl        | No    | No                                                  | Void                                          | Open Rakuten Login URL in the same browser's tab                               |
| hasUserSignedIn     | Yes   | No                                                  | Boolean                                       | Returns User Login Status                                                      |
| logout              | Yes   | (options?: [SDKCallbackParams](#sdkcallbackparams)) | Boolean                                       | Returns User Login Status                                                      |
| startSession        | Yes   | (options?: [SDKCallbackParams](#sdkcallbackparams)) | [UserPointInformation](#userpointinformation) | Start the user's session, generate Access Token using Refresh Token.           |
| refreshAccessToken  | Yes   | No                                                  | Void                                          | Refresh current Access Token using existing Refresh Token                      |
| setFeatureEnabled   | No    | boolean                                             | Void                                          | Enable/disable Mission JS SDK APIs                                             |
| setSDKPortalEnabled | No    | boolean                                             | Void                                          | Enable/disable SDK Portal                                                      |
| setUIEnabled        | No    | boolean                                             | Void                                          | Enable/disable UI Notification                                                 |
| setAccessToken      | No    | string                                              | Void                                          | Manually set Access Token                                                      |
| setRefreshToken     | No    | string                                              | Void                                          | Manually set Refresh Token                                                     |
| renewRefreshToken   | Yes   | string                                              | Void                                          | Renew Refresh Token. Not applicable for publishers who manage their own tokens |

### `Authentication UI`

| Function           | Async | Parameters          | Response | Description                                            |
| ------------------ | ----- | ------------------- | -------- | ------------------------------------------------------ |
| displayLoginButton | No    | (elementId: string) | Void     | Display Rakuten Reward SDK Login Button in the element |

<br /><br />

## `User`

### `User Functions`

| Function         | Async | Parameters                                          | Response                                      | Description                                              |
| ---------------- | ----- | --------------------------------------------------- | --------------------------------------------- | -------------------------------------------------------- |
| getUserName      | No    | No                                                  | String                                        | Returns Username's Full name                             |
| setUserName      | No    | No                                                  | String                                        | Set Username's Full name                                 |
| getUserInfo      | Yes   | (options?: [SDKCallbackParams](#sdkcallbackparams)) | [UserPointInformation](#userpointinformation) | Get User Information and current points                  |
| getMemberInfo    | Yes   | (options?: [SDKCallbackParams](#sdkcallbackparams)) | [MemberInformation](#memberinformation)       | Get Rakuten's Points member information                  |
| getIsUserConsent | No    | No                                                  | Boolean                                       | Get User's Consent status to Reward Mission terms of use |
| acceptConsent    | Yes   | (options?: [SDKCallbackParams](#sdkcallbackparams)) | Void                                          | Accept User's Consent to Reward Mission terms of use     |

### `User UI`

| Function            | Async | Parameters          | Response | Description                                                                                                         |
| ------------------- | ----- | ------------------- | -------- | ------------------------------------------------------------------------------------------------------------------- |
| displayLoginElement | No    | (elementId: string) | Void     | Display User Information (Name, Current Points, Unclaimed Points) if user logged in, or display Login Button if not |

<br /><br />

## `User Consent`

### `User Consent Functions`

| Function      | Async | Parameters                                          | Response | Description                                          |
| ------------- | ----- | --------------------------------------------------- | -------- | ---------------------------------------------------- |
| acceptConsent | Yes   | (options?: [SDKCallbackParams](#sdkcallbackparams)) | Void     | Accept User's Consent to Reward Mission terms of use |

### `User Consent UI`

| Function            | Async                                               | Parameters          | Response | Description                                    |
| ------------------- | --------------------------------------------------- | ------------------- | -------- | ---------------------------------------------- |
| displayConsentPopup | (options?: [SDKCallbackParams](#sdkcallbackparams)) | (elementId: string) | Void     | Display Mission SDK terms of use Consent Popup |

<br /><br />

## `Mission`

### `Mission Functions`

| Function    | Async | Parameters                                                                                                  | Response                                              | Description                     |
| ----------- | ----- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | ------------------------------- |
| getMissions | Yes   | (options?: [SDKCallbackParams](#sdkcallbackparams))                                                         | [Mission Item](#missionitem)[]                        | Returns list of Active Missions |
| logAction   | Yes   | (missionAction: [MissionActionData](#missionactiondata), options?: [SDKCallbackParams](#sdkcallbackparams)) | [MissionLogActionResponse](#missionlogactionresponse) | Returns log action response     |

### `Mission UI`

| Function           | Async | Parameters          | Response | Description                                              |
| ------------------ | ----- | ------------------- | -------- | -------------------------------------------------------- |
| displayMissionList | No    | (elementId: string) | Void     | Display active mission list using Mission SDK default UI |

<br /><br />

## `Claim Points`

### `Claim Points Functions`

| Function          | Async | Parameters                                                                                                | Response                                  | Description                      |
| ----------------- | ----- | --------------------------------------------------------------------------------------------------------- | ----------------------------------------- | -------------------------------- |
| getUnclaimedItems | Yes   | (options?: [SDKCallbackParams](#sdkcallbackparams))                                                       | [Unclaimed Item](#unclaimeditem)[]        | Returns list of unclaimed points |
| claimPointMission | Yes   | (pointActionData: [PointActionData](#pointactiondata), options?: [SDKCallbackParams](#sdkcallbackparams)) | [ClaimPointResponse](#claimpointresponse) | Returns claim point response     |

### `Claim Points UI`

| Function              | Async | Parameters          | Response | Description                                                |
| --------------------- | ----- | ------------------- | -------- | ---------------------------------------------------------- |
| displayUnclaimedItems | No    | (elementId: string) | Void     | Display unclaimed points list using Mission SDK default UI |

<br /><br />

## `Points History`

### `Points History Functions`

| Function         | Async | Parameters                                          | Response                          | Description                                          |
| ---------------- | ----- | --------------------------------------------------- | --------------------------------- | ---------------------------------------------------- |
| getPointHistory  | Yes   | (options?: [SDKCallbackParams](#sdkcallbackparams)) | [Points History](#pointhistory)[] | Returns list of points history for the past 3 months |
| getCurrentPoints | Yes   | (options?: [SDKCallbackParams](#sdkcallbackparams)) | [CurrentPoints](#currentpoints)   | Returns user's current points                        |

<br /><br />

## `Mission SDK Portal`

### `Mission SDK Portal Functions`

| Function         | Async | Parameters                                          | Response | Description                |
| ---------------- | ----- | --------------------------------------------------- | -------- | -------------------------- |
| displaySDKPortal | No    | (options?: [SDKCallbackParams](#sdkcallbackparams)) | Void     | Display Mission SDK Portal |

### `Mission SDK Portal UI`

| Function            | Async | Parameters                                                                                                                   | Response | Description                                       |
| ------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------- | -------- | ------------------------------------------------- |
| displayPortalButton | No    | (elementId: string, options?: [SDKCallbackParams](#sdkcallbackparams))                                                       | Void     | Display UI Default Button to open SDK Portal      |
| displayRewardIcon   | No    | (elementId: string, iconOptions: [RewardIconOptions](#rewardiconoptions), options?: [SDKCallbackParams](#sdkcallbackparams)) | Void     | Display UI Default Reward Icon to open SDK Portal |

<br /><br />

## `Other Pages`

### `Other Pages Functions`

| Function       | Async | Parameters | Response | Description                                   |
| -------------- | ----- | ---------- | -------- | --------------------------------------------- |
| openFaqUrl     | No    | No         | Void     | Open Mision SDK FAQ page in new tab           |
| openTncUrl     | No    | No         | Void     | Open Mision SDK Terms of Use page in new tab  |
| openPrivacyUrl | No    | No         | Void     | Open Mision SDK Privacy Terms page in new tab |

<br /><br />

# Class Object

### SDKInitParams

| Key              | Type       | Mandatory | Default Value | Description                                                                                                                                   |
| ---------------- | ---------- | --------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| appKey           | string     | Mandatory |               | Publisher's application Key                                                                                                                   |
| language         | 'ja', 'en' | Optional  | 'ja'          | Language used in Mission Reward SDK                                                                                                           |
| uiEnabled        | boolean    | Optional  | true          | Configuration to display our Achieve Mission Notification Banner                                                                              |
| featureEnabled   | boolean    | Optional  | true          | Configuration to display our Mission SDK features. Disabling this Key will make you can't use our Mission SDK features.                       |
| sdkPortalEnabled | boolean    | Optional  | true          | Configuration to display our Mission SDK Portal UI. Disabling this Key will make you can't use our Mission SDK Portal UI.                     |
| adId             | string     | Optional  | ''            | Device Ad Id, used in our Ads features as user identifier                                                                                     |
| accessToken      | string     | Optional  | ''            | Access Token generated by API-C, used to access Mission SDK's API                                                                             |
| refreshToken     | string     | Optional  | ''            | Refresh Token generated by API-C, used to acquire new or refresh the Access Token when it's expired. Mandatory if you passed `accessToken`.   |
| userName         | string     | Optional  | ''            | User's name, used to display user's name in SDK Portal. If empty,  user's full name is displayed in the Portal Popup                |
| successCallback  | void       | Optional  | undefined     | Function to be called after Mission SDK finishes initialization. Can be used to pass callback function such as page visit mission achievement |
|                  |            |           |               |                                                                                                                                               |

### SDKCallbackParams

| Key             | Type     | Mandatory | Default Value | Description                                                |
| --------------- | -------- | --------- | ------------- | ---------------------------------------------------------- |
| successCallback | Function | Optional  | undefined     | Function to be called after function successfully finished |

### MissionActionData

| Key                      | Type    | Mandatory | Default Value | Description                                                 |
| ------------------------ | ------- | --------- | ------------- | ----------------------------------------------------------- |
| actionCode               | string  | Mandatory | ''            | Mission Action Code                                         |
| forceDisplayConsentPopup | boolean | Optional  | false         | Force display User Consent Popup if user is not consent yet |

### MissionCompleteResponse

| Key      | Type                        | Default Value | Description                    |
| -------- | --------------------------- | ------------- | ------------------------------ |
| mission  | [MissionItem](#missionitem) | {}            | Mission Item Data              |
| success  | boolean                     | false         | Achieve Mission Request Status |
| achieved | boolean                     | false         | Achieve Mission Status         |

### PointActionData

| Key             | Type   | Mandatory | Default Value | Description                                                                       |
| --------------- | ------ | --------- | ------------- | --------------------------------------------------------------------------------- |
| actionCode      | string | Mandatory | ''            | Mission Action Code                                                               |
| achievedDateStr | string | Mandatory | ''            | Mission Achievement Date, without dash (`-`). Format: `YYYYMMDD`, e.g. `20231231` |

### UserPointInformation

| Key                    | Type   | Default Value | Description                                |
| ---------------------- | ------ | ------------- | ------------------------------------------ |
| unclaimedPoints        | number | 0             | User's unclaimed points                    |
| currentPoints          | number | 0             | User's current points                      |
| wallUrl                | string | ''            | URL for displaying Wall Ads                |
| fullScreenUrl          | string | ''            | URL for displaying Fullscreen Ads          |
| adportalUrl            | string | ''            | URL for displaying Ad Portal Ads           |
| missionadbanner_50Url  | string | ''            | URL for displaying Notification Banner 50  |
| missionadbanner_250Url | string | ''            | URL for displaying Notification Banner 250 |
| poikatsuUrl            | string | ''            | URL for displaying Poikatsu Ads            |

### MemberInformation

| Key          | Type   | Default Value | Description                          |
| ------------ | ------ | ------------- | ------------------------------------ |
| memberPoints | number | 0             | Current Rakuten's Points             |
| memberRank   | number | 0             | Current Rakuten's Points Member Rank |

### NotificationType

`'MODAL', 'BANNER', 'BANNER_50', 'BANNER_250', 'CUSTOM', 'NONE'`

### MissionItem

| Key              | Type                                  | Default Value | Description                                                            |
| ---------------- | ------------------------------------- | ------------- | ---------------------------------------------------------------------- |
| actionCode       | string                                | ''            | Mission Action Code, from Developer Portal                             |
| type             | string                                | ''            | Mission Type                                                           |
| iconurl          | string                                | ''            | URL for Mission Icon                                                   |
| instruction      | string                                | ''            | Mission Instruction                                                    |
| condition        | string                                | ''            | Mission Condition                                                      |
| notificationtype | [NotificationType](#notificationtype) | 'NONE'        | Mission Notification Banner Type                                       |
| point            | number                                | 0             | Points for Achieving Mission                                           |
| end              | datetime                              | ''            | Mission End Date Time                                                  |
| enddatestr       | string                                | ''            | Mission End Date in String Format. Format: `YYYYMMDD`, e.g. `20231231` |
| reachedCap       | boolean                               | 0             | Is Mission Already Reached Cap                                         |
| times            | number                                | 0             | Mission Maximum Achievements Allowed                                   |
| progress         | number                                | 0             | Mission Achievement's Progress                                         |

### MissionItemComplete

| Key              | Type                                  | Default Value | Description                                                |
| ---------------- | ------------------------------------- | ------------- | ---------------------------------------------------------- |
| name             | string                                | ''            | Mission Name                                               |
| instruction      | string                                | ''            | Mission Instruction                                        |
| iconurl          | string                                | ''            | URL for Mission Icon                                       |
| actionCode       | string                                | ''            | Mission Action Code, from Developer Portal                 |
| point            | string                                | ''            | Points for Achieving Mission                               |
| unclaimed        | string                                | ''            | Mission Unclaimed Point                                    |
| achieveddatestr  | string                                | ''            | Mission Achieved Date. Format: `YYYYMMDD`, e.g. `20231231` |
| notificationtype | [NotificationType](#notificationtype) | 'NONE'        | Mission Notification Banner Type                           |

### MissionLogActionResponse

| Key      | Type                                        | Default Value | Description                                                               |
| -------- | ------------------------------------------- | ------------- | ------------------------------------------------------------------------- |
| mission  | [MissionItemComplete](#missionitemcomplete) | {}            | Mission details                                                           |
| success  | Boolean                                     | false         | Mission log action status                                                 |
| achieved | [MissionItemComplete](#missionitemcomplete) | {}            | Mission achievement status. Validation if user is able to claim the point |
| member   | { unclaimed: number }                       | {}            | Returns User's total unclaimed points                                     |

### UnclaimedItem

| Key                    | Type                                                           | Default Value | Description                                                       |
| ---------------------- | -------------------------------------------------------------- | ------------- | ----------------------------------------------------------------- |
| achievedDate           | string                                                         | ''            | Mission Achievement Data. Format: `YYYY-MM-DD`, e.g. `2023-12-31` |
| unclaimedPoints        | number                                                         | ''            | How many unclaimed points to be claimed                           |
| unclaimedTimes         | number                                                         | ''            | How many times mission achieved                                   |
| pointsPerClaim         | number                                                         | ''            | How many points per mission achievement                           |
| actionCode             | string                                                         | ''            | Mission's Action Code                                             |
| actionPointName        | string                                                         | 'NONE'        | Mission's Name                                                    |
| actionPointInstruction | string                                                         | 0             | Mission's Instruction                                             |
| iconHref               | string                                                         | ''            | URL for Mission's icon                                            |
| notificationType       | 'MODAL', 'BANNER', 'BANNER_50', 'BANNER_250', 'CUSTOM', 'NONE' | ''            | Mission's Notification Type                                       |
| claimPointMission      | Function((options?: [SDKCallbackParams](#sdkcallbackparams)))  | ()            | Function to claim the point                                       |

### ClaimPointResponse

| Key             | type    | Default Value | Description                                           |
| --------------- | ------- | ------------- | ----------------------------------------------------- |
| actionCode      | string  | ''            | Mission Action Code                                   |
| claimTargetDate | number  | 0             | Claim Point Date. Format: `YYYYMMDD`, e.g. `20231231` |
| pointClaimed    | number  | 0             | How many points claimed                               |
| enableMissionAd | boolean | false         | Display / Hide Mission Ad                             |

### PointHistory

| Key    | type   | Default Value | Description                              |
| ------ | ------ | ------------- | ---------------------------------------- |
| points | number | 0             | How many points claimed in that month    |
| month  | string | ''            | Month. Format: `YYYYMMDD`, e.g. `202312` |

### CurrentPoints

| Key    | type   | Default Value | Description                                                     |
| ------ | ------ | ------------- | --------------------------------------------------------------- |
| date   | string | ''            | Date of Current Points. Format: `YYYY-MM-DD`, e.g. `2023-12-31` |
| points | number | ''            | Current Points                                                  |

### RewardIconOptions

| Key      | type                                                 | Default Value | Description                       |
| -------- | ---------------------------------------------------- | ------------- | --------------------------------- |
| position | `'topLeft', 'topRight', 'bottomLeft', 'bottomRight'` | 'topRight'    | Position of Unclaimed Points Info |
| height   | number                                               | 48            | Height of Reward Icon             |
| width    | number                                               | 48            | Width of Reward Icon              |

## `Error Codes`

| Key                              | Message                                                               | Description                                                                                                                                                                                                                                  |
| -------------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `error_no_refresh_token`         | You haven't provided refresh token, or refresh token invalid          | You manage the login but haven't provided the refresh token when [inititliaze](#sdkinitparams) Mission JS SDK, or the refresh token you provided already expired. You need to pass the valid refresh token when initializing Mission JS SDK. |
| `error_no_access_token`          | You haven't provided access token                                     | You manage the login but haven't provided the access token when [inititliaze](#sdkinitparams) Mission JS SDK. You need to pass the valid access token when initializing Mission JS SDK.                                                      |
| `error_feature_setting_disabled` | Feature Setting Disabled                                              | You disabled the feature settings, so you can't call our API. You need to enable the feature by calling the [`setFeatureEnabled`](#authentication) function.                                                                                 |
| `error_ui_setting_disabled`      | Feature Setting Disabled                                              | You disabled the UI settings, so you can't display the UI Notification. You need to enable the feature by calling the [`setUIEnabled`](#authentication) function.                                                                            |
| `error_not_start_session`        | You haven't start the session                                         | There's no access token defined, because you maybe haven't started the session. You need to call [`startSession`](#authentication) function to start the session.                                                                            |
| `error_cannot_start_session`     | You cannot start the session because you manage the token by yourself | Mission JS SDK can't refresh the access token because manage your own login state by passing access token. You need to call [`setAccessToken`](#authentication) function to manually set the access token.                                   |
| `error_logout_failed`            | Local storage cleared, but logout API failed                          | There's an error when revoking user's access token. But, worry not, the access token validity time is short, and Mission JS SDK already cleared the local storage.                                                                           |
| `error_no_username_because_omni` | You cannot get username because you manage the token by yourself      | You manage the login but didn't pass the user's full name. You can set the user's name by calling [`setUserName`](#user-functions).                                                                                                          |
| `error_not_login`                | You're not logged in                                                  | The user hasn't logged in. You can follow this [Authentication](./README.md#authentication) guideline to handle the login state.                                                                                                             |
| `error_refresh_token_invalid`    | Refresh token invalid, please try again                               | The refresh token you provided is invalid and the access token cannot be renewed. You need to pass the valid refresh token by calling [`setRefreshToken`](#authentication).                                                                  |
| `error_access_token_invalid`     | Access token invalid, please try again                                | The access token you provided is invalid. You need to pass the valid access token by calling [`setAccessToken`](#authentication).                                                                                                            |
| `error_action_still_invalid`     | The action is still invalid, please wait for a while                  | The mission you're trying to log action is still invalid, please wait for a while. This error is usually for fraud prevention, to prevent users sending log action multiple times in a short time.                                           |
| `error_user_not_consent`         | Unavailable For Legal Reasons                                         | User has not given their consent to Reward Mission SDK terms of usage. You need to accept the consent first by calling the [`displayConsentPopup`](#user-consent-ui) function to display User Consent Popup.                                 |
| `error_not_initialized`          | You have not initialized the SDK                                      | You haven't initialized Mission SDK. Please call SDK's [`init`](./README.md#initialize-mission-sdk) to initialize SDK and pass the required params                                                                                           |
