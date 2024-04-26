set -e

git clone --depth 1 https://github.com/pi-hole/pi-hole.git

if [[ -d "./pi-hole/automated install/" ]]; then
   pushd "pi-hole/automated install/"
   bash ./basic-install.sh
   popd
else
    echo "Failed to install pihole."
    exit 1
fi

if [[ -f "./pihole-adlist.txt" ]]; then
    echo "Updating adlist..."
    python3 update-adlist
else
    echo "Unable to update adlist."
    exit 1
fi
