# Note
I recommend running this script and Pi-Hole on a virtual machine,
Raspberry-Pi, or other dedicated machine. The Pi-Hole install script
needs to be run with root permissions. Find out more [here](about.md).

The images below are from a new virtual machine running Ubuntu 24.04.

# Requirements
- [Pi-Hole Supported Operating System](https://docs.pi-hole.net/main/prerequisites/#supported-operating-systems)
- git
- python

# Install

##Clone the repository
``` shell
git clone https://github.com/hholb/home-netsec
cd home-netsec
```

##Run the install script

Run `install.sh`. It must be run as root for the Pi-Hole installer to
work correctly.
``` shell
sudo ./install.sh
```

This downloads and runs the Pi-Hole installation script from the official Pi-Hole
repository. It will ask you a few questions along the
way. I will walk through each step below.

Move through the menu screens by pressing `Enter` or typing one of
the highlighted characters. Move the cursor with the left and right
arrow keys.

Pi-Hole needs its host device IP address to be static for other devices on your
network to reliably communicate with it.
!!TODO

# Uninstall

Uninstall Pi-Hole
``` shell
sudo ./uninstall.sh
```

Remove this repository

``` shell
cd ..
rm -r home-netsec
```
