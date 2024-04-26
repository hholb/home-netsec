#!/usr/bin/env bash

set -e

# clone the pi-hole repo if it isn't already here
if ! [[ -d "./pi-hole" ]]; then
    git clone --depth 1 https://github.com/pi-hole/pi-hole.git
fi

# run the pi-hole install script
if [[ -d "./pi-hole/automated install/" ]]; then
    pushd "pi-hole/automated install/"
    PIHOLE_SKIP_OS_CHECK=true bash ./basic-install.sh
    popd
else
    echo "Failed to install pihole."
    exit 1
fi

# update the adlists in the database
if [[ -f "./adlist.txt" ]]; then
    echo "Updating adlist..."
    python3 update-adlist.py
else
    echo "Unable to update adlist."
    exit 1
fi

# tell pihole to pull the domains from the new adlists
pihole -g
