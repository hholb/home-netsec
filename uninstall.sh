#!/usr/bin/env bash

set -e

# run the pihole uninstall script
if [[ -d "./pi-hole/automated install/" ]]; then
    pushd "./pi-hole/automated install/"
    bash uninstall.sh
    popd
else
    echo "Did not find uninstall script."
    exit 1
fi
