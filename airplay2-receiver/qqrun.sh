#!/bin/bash

podman build --http-proxy=false -f docker/Dockerfile .

imageid=$(
podman build -q --http-proxy=false -f docker/Dockerfile .
)
set -x

#  --group-add keep-groups \
#  --privileged \
#  --device=/dev/sr0 \
#  --device /dev/bus/usb \
#  --env ALSA_OUTPUT_CREATE=yes \
# TODO: still not work in podman container!
podman run -e AP2IFACE=eth0 \
 --device /dev/snd:/dev/snd \
 --rm -it ${imageid} 
set +x


