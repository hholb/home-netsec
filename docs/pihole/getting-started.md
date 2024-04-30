# Note
I recommend running this script and Pi-Hole on a virtual machine,
Raspberry-Pi, or other dedicated machine. The Pi-Hole install script
needs to be run with root permissions. Find out more [here](about.md).

The images below are from a new virtual machine running Ubuntu 24.04.

## Requirements
- [Pi-Hole Supported Operating System](https://docs.pi-hole.net/main/prerequisites/#supported-operating-systems)
- git
- python

## Install

### Download the phm script
``` shell
curl -sSL https://raw.githubusercontent.com/hholb/phm/main/phm > phm
chmod +x phm
```

### Install pihole

``` shell
./phm install
```

This downloads and runs the officaial Pi-Hole installation script from
the Pi-Hole repository. It will ask you a few questions along the
way. See the [User Guide](user-guide.md) for more details.

## Uninstall

### Uninstall Pi-Hole
``` shell
./phm uninstall
```

### Uninstall phm
``` shell
rm phm
```
