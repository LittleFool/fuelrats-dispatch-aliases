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

### irssi

Copy the contents of `irssi/add.ini` into the `((status))` window of irssi

### weechat

Copy the contents of `weechat/add.ini` into the server window of weechat

### Revolution-IRC

Make a backup within the App `Settings -> Backup -> Create a new backup`. Repalce the `command_aliases.json` inside the `.zip` file with the `revolution-irc/command_aliases.json` file from this repository.
Restore the modified `.zip` file in the App `Settings -> Backup -> Restore a backup`

### The Lounge

Ensure that [thelounge-plugin-shortcuts](https://github.com/minidigger/thelounge-plugin-shortcuts) is installed.
Copy the contents of `TheLounge/add.ini` into a server window.

## Usage

See [the Usage Guide](USAGE.md)

## Uninstall

### mIRC

Press `ALT+R`, then switch to the `Aliases` tab. Remove all entries you have copied from `mIRC/aliases.ini`.

### AdiIRC

Press `ALT+R`, then right click on the aliases file and choose unload or delete. Click save and close in the bottom left.

### HexChat

Close HexChat. Open a file browser and go to the folder for your OS:

* Windows: `%APPDATA%\HexChat`
* Microsoft Store: `%LOCALAPPDATA%\Packages\39215TingPing.HexChat_fqe8h3fzrj50c\LocalCache\Roaming\HexChat`
* Unix: `~/.config/hexchat`
* Flatpak: `~/.var/app/io.github.Hexchat/config/hexchat`
* Snap: `~/snap/hexchat/current/.config/hexchat`

If you have other aliases you want to keep edit the `commands.conf` file and remove all unwanted aliases.
If you want to go back to default delete the `commands.conf` file or replace it with `HexChat\commands-default.conf`

### Kiwi IRC

Go to Kiwi settings, switch to the `Aliases` tab and remove all unwanted aliases.

### irssi

Copy the contents of `irssi/remove.ini` into the `((status))` window of irssi

### weechat

Copy the contents of `weechat/remove.ini` into the server window of weechat

### Revolution-IRC

Make a backup within the App `Settings -> Backup -> Create a new backup`. Clear the `command_aliases.json` inside the `.zip` file. Restore the modified `.zip` file in the App `Settings -> Backup -> Restore a backup`

### The Lounge

Ensure that [thelounge-plugin-shortcuts](https://github.com/minidigger/thelounge-plugin-shortcuts) is installed.
Copy the contents of `TheLounge/remove.ini` into a server window.

## Credits

Thanks for the translations to:

* Whirlwind113 - Russian
* Pistou - French
* Aarkein - Spanish
* KumaKenji - Portuguese
* NivisOwl - Chinese
* Sintoreni - Italian
* Yuri_Voskov - Polish
* anonymous - Czech
* Ramnos - Turkish
* anonymous - Hungarian
