# home-netsec
This repository contains code for installing and configuring the
Pi-Hole. It uses the [official Pi-Hole install](#TODO) script, then
adds the domains listed in `pihole-adlist.txt` to the Pi-Hole
database.

## Usage

### Clone the repo
``` shell
git clone https://github.com/hholb/home-netsec.git
cd home-netsec
```

### Run the setup script
``` shell
bash pihole-setup.sh
```

### Check that the Pi-Hole is running
``` shell
pihole status
```
