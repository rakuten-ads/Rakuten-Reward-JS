# `FAQ`

Table of Contents

- [Does Mission JS SDK uses any Front End Framework, like React, Vue, or Angular?](#does-mission-js-sdk-uses-any-front-end-framework-like-react-vue-or-angular)
- [I use React/Vue/Angular in my website, is there any possible conflicts with the Mission JS SDK](#i-use-reactvueangular-in-my-website-is-there-any-possible-conflicts-with-the-mission-js-sdk)
- [Does Mission JS SDK collect user's Advertising ID?](#does-mission-js-sdk-collect-users-advertising-id-ad-id)
- [My website is not using Rakuten OMNI Auth, can I use Mission JS SDK?](#my-website-is-not-using-rakuten-omni-auth-can-i-use-mission-js-sdk)
- [I have a daily launch app mission. How should I implement it?](#i-have-a-daily-launch-app-mission-how-should-i-implement-it)
- [How do I claim mission after a mission is achieved?](#how-do-i-claim-mission-after-a-mission-is-achieved)
- [How can I implement the custom notification UI?](#how-can-i-implement-the-custom-notification-ui)
- [Is it possible to detect SDK Portal closed event?](#is-it-possible-to-detect-sdk-portal-closed-event)
- [What will happen if Access Token is expired?](#what-will-happen-if-access-token-is-expired)
- [User A already accept to Mission SDK's User Consent but then logged out, then User B login in the same browser. What is the Consent Status for User B?](#user-a-already-accept-to-mission-sdks-user-consent-but-then-logged-out-then-user-b-login-in-the-same-browser-what-is-the-consent-status-for-user-b)
- [How to send tracking events?](#how-to-send-tracking-events)
- [I don't want to display SDK Portal UI, because I want to create and use our custom UI. How to disable SDK Portal?](#i-dont-want-to-display-sdk-portal-ui-because-i-want-to-create-and-use-our-custom-ui-how-to-disable-sdk-portal)
- [I want every users to accept user consent before achieving any missions. How can I do that?](#i-want-every-users-to-accept-user-consent-before-achieving-any-missions-how-can-i-do-that)

## Does Mission JS SDK uses any Front End Framework, like React, Vue, or Angular?

<details>
<summary>Answer</summary>
Mission JS SDK is written in Vanilla Javascript without any Front End Frameworks. We have some reasons not to use any frameworks, such as:

- Keep JS SDK file small
- Avoid any conflicts with publisher's websites
- Have better browsers support
  </details>

## I use React/Vue/Angular in my website, is there any possible conflicts with the Mission JS SDK

<details>
<summary>Answer</summary>
As we mentioned before, Mission JS SDK is written in Vanilla Javascript, so there should be no issues of conflicts with your website's tech stack.

Please let us know if you find any conflicts with Mission JS SDK.

</details>

## Does Mission JS SDK collect user's Advertising ID (Ad-ID)?

<details>
<summary>Answer</summary>
No, because browsers don't have access to collect user's Advertising ID (Ad-ID). But, if there's any use case from publishers to pass the Ad-ID, you can pass the user's Ad-ID during the Mission JS SDK initialization.

```javascript
rewardSDK.init({
	appKey: "QWERTYUIOPASDFGHJKLZXCVBNM123456789",
	language: "ja",
	adId: "ABCD1234567H",
});
```

</details>

## My website is not using Rakuten OMNI Auth, can I use Mission JS SDK?

<details>
<summary>Answer</summary>
If you haven't used Rakuten OMNI Auth, then it's not possible to share the login state between your website and JS SDK. But, you can still use our Mission JS SDK by using one of this login feature: <a href="#sdk-handles-the-login"> SDK handles the login</a>

</details>

## I have a daily visit website mission. How should I implement it?

<details>
<summary>Answer</summary>
To achieve the mission's action everytime user visit the website or visit any pages, you should wait for the SDK to finish all the initialization and data API fetch to verify the user and SDK.

That's why you can't log action directly after init the JS SDK like this:

```javascript
rewardSDK.init({
	appKey: "QWERTYUIOPASDFGHJKLZXCVBNM123456789",
	language: "ja",
});

rewardSDK.logAction({ actionCode: "ABCD123456" }); // this function will return error, because Mission JS SDK isn't finished initialized.
```

In order to log the action or call any callbacks after JS SDK finishes the initialization, you can pass the `successCallback` function during the initialization.

```javascript
const rewardSDK = window.RewardMissionSDK || {};

rewardSDK.init({
	appKey: "QWERTYUIOPASDFGHJKLZXCVBNM123456789",
	language: "ja",
	successCallback: () => {
		console.log("Callback after JS SDK Init");
		rewardSDK.logAction({ actionCode: "ABCD123456" }); // log this action after SDK initialization finished.
	},
});
```

Or, you can use async/await and put the codes sequentially.

```javascript
(async () => {
	try {
		await rewardSDK.init({
			appKey: "QWERTYUIOPASDFGHJKLZXCVBNM123456789",
			language: "ja",
		});
	} catch (err) {
		// to catch init/authentication error
	}

	rewardSDK.logAction({ actionCode: "ABCD123456" }); // log this action after SDK initialization finished.
})();
```

</details>

## How do I claim mission after a mission is achieved?

<details>
<summary>Answer</summary>
Claim API is available in the <a href="./README.md#unclaimeditem">UnclaimedItem</a> object as `claimPointMission` function. To claim the point, there are 2 ways:

<br />

1. Call the `claimPointMission` API after user achieved a mission. But, this function is only available if the user already completed all the actions.

For example, we have Mission A that requires users to visit the page 3 times. After the user completed 3 times visit, you can call the `claimPointMission` API.
But, if the user hasn't completed all the actions, then they can't claim the point yet.

```javascript
// async/await supported
const missionResponse = await rewardSDK.logAction({ actionCode: "ABCD12345" });
missionResponse.claimPointMission();

// Promise-based
reward.logAction({ actionCode: "ABCD12345" }).then((missionResponse) => {
	missionResponse.claimPointMission();
});
```

2. Call the Unclaimed items API to get all the unclaimed points, and then call `claimPointMission` API for the point you want to claim.

```javascript
// async/await supported
const unclaimedItems = await rewardSDK.getUnclaimedItems();
const targetMission = unclaimedItems.find(
	(unclaimedItem) => unclaimedItem.actionCode === "ABCDE123456"
);
if (targetMission) targetMission.claimPointMission();

// Promise-based
reward.getUnclaimedItems().then((unclaimedItems) => {
	const targetMission = unclaimedItems.find(
		(unclaimedItem) => unclaimedItem.actionCode === "ABCDE123456"
	);
	if (targetMission) targetMission.claimPointMission();
});
```

</details>

## Do I have to call `logout` API function when user logged out?

<details>
<summary>Answer</summary>
Yes, you need to call the logout API when the user is logged out in your website, to make sure all the tokens are cleared in the browser and in our database, by calling our `logout` function.

```javascript
rewardSDK.logout();
```

</details>

## How can I implement the custom notification UI?

<details>
<summary>Answer</summary>
For example, we have Mission A and we want to display custom Notification UI after the user achieved the mission.

```javascript
const displayCustomNotifUI = () => console.log("Display UI");

try {
	const response = await rewardSDK.logAction({ actionCode: "ABCD123456" });

	const isAchieveMissionSuccess = response.success && response.achieved; // check if achieve mission success & achieved
	const isCustomNotification = response.mission.notificationtype === "CUSTOM"; // check if the notification for the mission is CUSTOM
	const isUIEnabled = rewardSDK.getUIEnabled(); // check if the user enables UI Notification feature

	if (isAchieveMissionSuccess && isCustomNotification && isUIEnabled) {
		// Display Custom Notification UI here.
		displayCustomNotifUI();
	}
} catch (e) {
	// do some error handling
}
```

</details>

## Is it possible to detect SDK Portal closed event?

<details>
<summary>Answer</summary>
Yes, it is possible to pass the detect SDK Portal closed event by providing the `closeCallback` when calling the `displaySDKPortal` or when displaying our Button to open SDK Portal.

```javascript
const closeCallback = () => console.log("SDK Portal Closed");

// call displaySDKPortal function
rewardSDK.displaySDKPortal({ closeCallback });

// display SDK Portal from SDK Button
const sdkPortalButtonElementId = "sdk-portal-button";
rewardSDK.displayPortalButton(sdkPortalButtonElementId, { closeCallback });

// display Reward Icon to open SDK Portal
const sdkPortalRewardIconElementId = "sdk-portal-reward-icon";
rewardSDK.displayRewardIcon(
	sdkPortalRewardIconElementId,
	{ position: "topRight" },
	{ closeCallback }
);
```

</details>

## What will happen if Access Token is expired?

<details>
<summary>Answer</summary>
Mission JS SDK will automatically requests a new valid Access Token using the existing Refresh Token. So, please make sure that you always provide a valid refresh token to make this feature works.

</details>

## User A already accept to Mission SDK's User Consent but then logged out, then User B login in the same browser. What is the Consent Status for User B?

<details>
<summary>Answer</summary>
User Consent feature is tied with the user's account, not the browser side. So, User B has a different consent status with User A.

</details>

## How to send tracking events?

<details>
<summary>Answer</summary>
Currently, Mission JS SDK doesn't provide built-in tracking, but we're working on building our own events tracking. If you want to send events tracking when using our SDK APIs, here are some ways to send them.

Let'say you want to send tracking events using Rakuten Analytics (RAT) to send analytics data when users achieving a mission.

1. Before calling our `logAction` API

```javascript
function logAction() {
	// sending log action event
	window.RAT.addCustomEvent({
		accountId: 123,
		serviceId: 123,
		pData: {
			key: "value",
		},
	});
	rewardSDK.logAction({ actionCode: "ABCDEFGH123" });
}
```

2. Using `successCallback` object to pass your tracking functions after users succesfully achieved the mission.

```javascript
function logAction() {
	rewardSDK.logAction(
		{ actionCode: "ABCDEFGH123" },
		{
			successCallback: () => {
				// send success log action event
				window.RAT.addCustomEvent({
					accountId: 123,
					serviceId: 123,
					pData: {
						key: "value",
					},
				});
			},
		}
	);
}
```

3. Using `try & catch` approach to send tracking events if user failed to achieve the mission or there's an issue during the mission achievement.

```javascript
function logAction() {
	try {
		rewardSDK.logAction({ actionCode: "ABCDEFGH123" });
	} catch (error) {
		// send failed log action event
		window.RAT.addCustomEvent({
			accountId: 123,
			serviceId: 123,
			pData: {
				key: "value",
				error,
			},
		});
	}
}
```

</details>

## I don't want to display SDK Portal UI, because I want to create and use our custom UI. How to disable SDK Portal?

<details>
<summary>Answer</summary>
You can disable our SDK Portal UI by passing `sdkPortalEnabled` key during the Mission JS SDK's initialization.

```javascript
rewardSDK.init({
	appKey: "QWERTYUIOPASDFGHJKLZXCVBNM123456789",
	language: "ja",
	adId: "ABCD1234567H",
	sdkPortalEnabled: false,
});
```

By passing `sdkPortalDisabled = true`, users won't be able to see SDK Portal, and won't see SDK Portal Button when claiming point.

</details>

## I want users to accept user consent before achieving any missions. How can I do that?

<details>
<summary>Answer</summary>
Sure, you can follow this:

```javascript
rewardSDK.logAction({
	actionCode: "12345ABCDE",
	forceDisplayConsentPopup: true,
});
```

You can pass the [`forceDisplayConsentPopup`](./API.md#missionactiondata) when calling our `logAction` API. So, if any users want to do the log action, they need to give their consent first.

</details>
