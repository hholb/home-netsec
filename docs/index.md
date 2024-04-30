# phm - Hayden's [pihole](https://pi-hole.net) manager

- [About](pihole/about.md)
- [Getting Started](pihole/getting-started.md)
- [User Guide](pihole/user-guide.md)

## Basic Usage

See [Getting Started](pihole/getting-started.md) or
the [User Guide](pihole/user-guide.md) for more information.

`phm` is a command-line program written in python for installing and
managing a pihole installation.

### View help-text and options
``` shell
phm --help
```

### Install pihole
``` shell
phm install
```

### See pihole status
``` shell
phm status
```

### Add more ad lists to the database
``` shell
phm add-adlist adlist.txt
```

### Update pihole
``` shell
phm update
```

### Remove pihole
``` shell
phm uninstall
```
