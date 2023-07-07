# ResidentFlash
This repository have sources for packages of my Terminal Emulator based on Linux

## How to install
To install Standart you need go to [mediafire](https://www.mediafire.com/file/l1mlcwh5qj5k213/Standart-1.1.zip/file) to download the program files and extract to a folder on your computer.

## Starting with Standart 
After install I recommend you use tree commands everyday after use:

- `mail` Show the announcements of developer team. Update hourly
- `sync` Download and Update Installed version of Standart
- `sl update` Update mirrors for sl (Standart Listback) package manager

## Commands
Available commands for Standart v1.2

- `alias [name - command]` Create aliases
- `exit` Quit from Terminal
- `clear` Clear Terminal 
- `dir` `ls [dirname]` List files and folder on directory
- `pwd` Show current working directory
- `yes [text]` Print repeatedly a string on Terminal
- `local [command]` Run a command on Shell or CMD
- `prompt [text]` Ask anything to users
- `seq [number]` Make numeral sequence from until selected number
- `sl` Default Standart package manager
- `version` Show installed version of Standart
- `mkdir [dirname]` Create a directory
- `rmdir [dirname]` Delete a directory
- `rm [filename]` Delete a file
- `cp [source - new name]` Copies files 
- `mv [source - new name]` Move files
- `cat [filename]` Show file contents on Terminal
- `touch [filename]` Clear file contents and create ones
- `server [int: PORT]` Start localhost server on inserted port
- `intro` Show release notes
- `wget [url] [filename]` Download files from internet
- `sync` Update local Standart version
- `unalias [name]` Delete aliases
- `install [filename]` Install your python code as a Standart Package
- `help [document]` Show help document 
- `mail` Show announcements from development team

## Interactive Colors on Terminal
If you're trying use colors on Terminal, Standart have this function,
it's work on `echo` to print your text and `cat` that show a content of 
a file. See the colors code below:

```
&black	 &red		
&green	 &yellow
&blue    &purple
&cian    &white

&bold    &italic
&sublime
```
And you can use & to get other values on your text. See codes below:
- `&appname` Replaced by name of vmlinux
- `&version` Replaced by version of vmlinux
- `&hostname` Replaced by name of computer
- `&ipadress` Replaced by ip adress of computer
- `&system` Replaced by installed system on your computer
- `&root` Replaced by vmlinux installation path 
- `&time` Replaced by current time
