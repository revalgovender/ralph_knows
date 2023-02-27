# Ralph Knows

![Ralph image](/img/ralph.jpg)

## About
Discord bot which provides useful information for AOE2DE.

## Usage
You can interact with Ralph by using the following slash commands:

### Counter
There are two ways you can use this command. You can use to retrieve text based responses or audio responses.

#### Text responses
`/counter` and then supply a unit to look up the counter for.

#### Audio responses
- Join a voice channel
- Run `/join`
- Ralph will join your voice channel
- Run `/counter`
- Ralph will return a text response in the text channel
- Ralph will return an audio response in the voice channel
- If the counter list is too long, Ralph will only speak the first two

#### Example input:
![usage image](/img/auto-complete-usage.png)

#### Result:
![usage image](/img/counter-result.png)
![usage image](/img/voice-usage.png)

### Civ Information
`/civ` and then select the civ you want information on

#### Example input:
![usage image](/img/civ-usage.png)

#### Result:
![usage image](/img/civ-result.png)

### Build Orders
`/build-order` and then select the build order you want instructions for from the list provided

#### Example input:
![usage image](/img/build-order-usage.png)

#### Result:
![usage image](/img/build-order-result.png)

## Bot Availability
- Bot is currently running as and when needed
- If usage is low, we will reconsider bot availability

## Deployment
- Deployments are done automatically whenever there is a new commit pushed to the remote "main" branch
- This is configured in Heroku

## Reporting Issues
- If Ralph can't find the unit you are looking for, he will record your submission and will consider it for the future.
- Report any issues to @revalgovender or `REVZ-ZN#8884` on Discord.
