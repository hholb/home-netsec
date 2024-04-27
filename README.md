# phm
This repository contains `phm`, a CLI tool for installing and updating the
Pi-Hole. Under the hood, `phm` uses the [official Pi-Hole install](#TODO) script, then
adds the domains listed in `adlist.txt` to the pihole's database.

## Setup
### Requirements
- python3

### Download `phm`
``` shell
curl https://raw.github.usercontent.com/hholb/phm/main/phm > phm
```

## Usage
### Run `phm --help`
``` shell
./phm --help
```

### Check that the Pi-Hole is running
``` shell
./phm status
```
