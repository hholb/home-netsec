# phm
This repository contains `phm`, a CLI tool for installing and updating the
Pi-Hole. Under the hood, `phm` uses the [official Pi-Hole install](#TODO) script, then
adds the domains listed in `adlist.txt` to the pihole's database.

## Usage

### Download `phm`
``` shell
curl -
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
