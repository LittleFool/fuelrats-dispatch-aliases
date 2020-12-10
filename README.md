# Fuel Rats Dispatch Aliases
These aliases are ment to help a Fuel Rats diaspatcher to more efficiently dispatch cases, specially in foreign languages or on a high case load.

## Installation

### mIRC
In mIRC press `ALT+R`, then switch to the `Aliases` tab. Copy and Paste the content of the `mIRC/aliases.ini` from this repository into there and click OK to save the changes.

### AdiIRC
In AdiIRC press `ALT+R`, then click on `File` - `New`. Copy and paste the content of the `AdiIRC/aliases.ini` from this repository into the editor. Then click on `File` - `Save`, enter a filename such as `aliases.ini` and save it under `%LOCALAPPDATA%\AdiIRC\Scripts` (default).

### HexChat
Close HexChat. Open a file browser and go to the folder for your OS:

* Windows: `%APPDATA%\HexChat`
* Microsoft Store: `%LOCALAPPDATA%\Packages\39215TingPing.HexChat_fqe8h3fzrj50c\LocalCache\Roaming\HexChat`
* Unix: `~/.config/hexchat`
* Flatpak: `~/.var/app/io.github.Hexchat/config/hexchat`
* Snap: `~/snap/hexchat/current/.config/hexchat`

Copy the `HexChat\commands.conf` into the folder. If you already have User Commands set up you have to merge the files or your Commands will be overwritten. When done start HexChat.

### Kiwi IRC
Go to Kiwi settings, switch to the `Aliases` tab, copy and paste the content of the `KiwiIRC/aliases.ini` from this repository into there.
**Be careful: /close syntax has changed and actually closes the case now**

### irssi
Copy the contents of `irssi/add.ini` into the `((status))` window of irssi

### weechat
Copy the contents of `weechat/add.ini` into the server window of weechat
This will override your `/close` alias which closes a window (buffer) the command for that is `/buffer close` so you might want to create a differen alias for that (don't use /bc) (don't ask me why i know that)

### Revolution-IRC
Make a backup within the App `Settings -> Backup -> Create a new backup`. Repalce the `command_aliases.json` inside the `.zip` file with the `revolution-irc/command_aliases.json` file from this repository.
Restore the modified `.zip` file in the App `Settings -> Backup -> Restore a backup`

## Credits
Thanks for the translations to:
* Whirlwind113 - Russian
* Pistou - French
* Aarkein - Spanish
* KumaKenji - Portuguese
* NivisOwl - Chinese
* Sintoreni - Italian
* Yuri_Voskov - Polish
