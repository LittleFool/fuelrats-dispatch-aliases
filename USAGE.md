# Usage Guide

## Introduction

This guide explains how to use these dispatch aliases. It is **not** a dispatching guide.

Aliases in IRC Clients are custom commands that are meant to make complex tasks quicker and easier.
The complexity between aliases varies between clients, not all clients support everything. Where some clients give you a whole scripting language other clients limit aliases to single lines of text.
In all IRC Clients, aliases are prefixed with a `/`. So the alias named `hello` would be executed with writing `/hello`.
With most, if not all clients, aliases can use parameters that make them useful. Parameters are usually just appended to the alias name with spaces. So if we have an alias `/hello` that sends a greeting we could add the name of the person we want to greet with `/hello Bob` and this would then replace the parameter in our alias with the value `Bob`. How you access parameters inside an alias varies from IRC Client to IRC Client and is not gonna be part of this guide.

In the sections below I'm gonna list all aliases in this repository, give their syntax, and an example.
Required parameters will be given just as a string e.g. `/hello name` means the parameter `name` is required. Optional parameters are written in square brackets, so `/hello [name]` means the parameter `name` might be omitted. If not stated otherwise all aliases are multilingual by appending the language like `/hello-fr` for french.

## Greeting / Prepping the client

---

Alias: `/hello [client1] [client2] [client3]`

Text: `Welcome to the Fuel rats, [client1] [client2] [client3]. Please tell us once you've powered down all of your modules EXCEPT life support, need help with it or if an "Oxygen depleted in:" timer appear in the upper right.`

---

Alias: `/eng [client1] [client2] [client3]`

Text: `[client1] [client2] [client3], do you speak english?`

Notes: only available as `/eng-language`. supports more languages than any other alias

---

Alias: `/off [client1] [client2] [client3]`

Text: `[client1] [client2] [client3] let us know once you've disabled all modules EXCEPT life support.`

---

Alias: `/offq [client1] [client2] [client3]`

Text: `[client1] [client2] [client3] did you turn off all your modules EXCEPT life support?`

---

Alias: `/o2 [client1] [client2] [client3]`

Text: `[client1] [client2] [client3] do you see a "oxygen depleted in ..." timer in the top right of your HUD?`

---

Alias: `/navsys [client1] [client2] [client3]`

Text: `[client1] [client2] [client3] please look in the left panel in the navigation tab and give me the full system name under "System" in the top left corner.`

## Normal Rescue

---

Alias: `/navsys [client1] [client2] [client3]`

Text: `[client1] [client2] [client3] please look in the left panel in the navigation tab and give me the full system name under "System" in the top left corner.`

---

Alias: `/open [client1] [client2] [client3]`

Text: `[client1] [client2] [client3] please exit to the main menu and log back in to OPEN play, then re-disable your thrusters.`

---

Alias: `/wing client1 [client2] [client3]`

Text:
> `client1 [client2] [client3] now, please invite your rat(s) to a wing.`
>
> `!wing client1 [client2] [client3]`

Notes: Not all Clients send the `!wing` fact.

---

Alias: `/beacon client1 [client2] [client3]`

Text:
> `client1 [client2] [client3] lastly, enable your beacon so your rat(s) can find you in system.`
>
> `!beacon client1 [client2] [client3]`

Notes: Not all Clients send the `!beacon` fact.

---

Alias: `/bcalt [client1] [client2] [client3]`

Text: `[client1] [client2] [client3] please go to the Comms Menu on the top left, and from the third tab (where you invited your rats to the wing) under Options use 'Enable Wing Beacon'.`

---

Alias: `/eta client time`

Text: `client your rats will be with you in about time minutes, if you see a blue oxygen timer pop up at any time tell me immediately.`

Notes: `time` is in minutes.

---

Alias: `/sc [client1] [client2] [client3]`

Text:
> `[client1] [client2] [client3] looks like you're too close to a stellar body, please do the following:`
>
> `!sc [client1] [client2] [client3]`

Notes: Not all clients send the `!sc` fact.

---

Alias: `/scenter [client1] [client2] [client3]`

Text: `[client1] [client2] [client3] to enter supercruise open your left menu, navigation tab and select the main star in your current system (will be the first entry in the list), then press the jump button.`

---

Alias: `/scdrop [client1] [client2] [client3]`

Text: `[client1] [client2] [client3] to drop from supercruise slow down to 30km/s, open your left menu, navigation tab and select the main star in your current system (will be the first entry in the list), then press the jump button.`

---

Alias: `/close case# rat client`

Text:
> `client you should be receiving fuel now. Please remain with your rat for some quick and helpful tips on fuel management.`
>
> `!close case# rat`

Notes: Not all clients send the `!close` but most do so **this actually closes a case!**

## CR

---

Alias: `/mmconf [client1] [client2] [client3]`

Text: `[client1] [client2] [client3] please confirm that you've quit to main menu where you can see your ship in the hangar.`

---

Alias: `/crm [client1] [client2] [client3]`

Text: `[client1] [client2] [client3] from THIS point onwards, remain logged out in the Main Menu please! Do NOT login until I give you the "GO GO GO" command.`

---

Alias: `/cro2 [client1] [client2] [client3]`

Text: `[client1] [client2] [client3] without logging in, do you remember how much O2 you had left?`

---

Alias: `/crpos [client1] [client2] [client3]`

Text: `[client1] [client2] [client3] without logging in, can you remember WHERE in the system you were? By the star, a planet or station or on the way to one?`

---

Alias: `/mmsys [client1] [client2] [client3]`

Text: `[client1] [client2] [client3] staying in the main menu, can you confirm your full system name inlcuding any sector name? Look in the upper right below your CMDR name where it says / IDLE`

---

Alias: `/crvideo [client1] [client2] [client3]`

Text: `[client1] [client2] [client3] here is a short video on how to do it: <link>`

---

Alias: `/crgo client rat1 [rat2] [rat3]`

Text: `client GO GO GO! $1 1. Login to OPEN - 2. light your beacon - 3. invite your rats rat1 [rat2] [rat3] to a wing - 4. report your o2 time in this chat and be ready to logout if I tell you to.`

---

Alias: `/sorry client`

Text: `client sorry we couldn't get to you in time today, your rats will be there for you after you respawn to help you with some tips and tricks, so please stick with them for a bit.`

## Misc

---

Alias: `/ls [client1] [client2] [client3]`

Text: `[client1] [client2] [client3] please turn your Life Support on immediately: go to the right menu -> Modules tab, select Life Support and select Activate`

---

Alias: `/sr [client1] [client2] [client3]`

Text: `[client1] [client2] [client3] please disable Silent Running Immediately!  Default key: Delete, or in the Right side Holo Panel > SHIP tab > Functions Screen - Middle Right`

---

Alias: `/db [client1] [client2] [client3]`

Text: `[client1] [client2] [client3] For advice and information in <Language> please enter channel → #debrief ← either by clicking on it right here or entering /join #debrief in this channel, a tab will open left of the chat. Switch to it.`

---

Alias: `/psfrf5 client`

Text: `client please press OPTION on your controller, go to Social and press R1 and L1 a couple of times to refresh your friendslist`

Notes: only available in english
