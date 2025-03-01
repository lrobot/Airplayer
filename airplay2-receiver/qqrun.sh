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
#  --device /dev/snd:/dev/snd \
  #--privileged \
 #--device /dev/shm:/dev/shm \
#  --env ALSA_OUTPUT_CREATE=yes \
# TODO: still not work in podman container!
 #-v /var/lib/dbus:/var/lib/dbus \
  #-v /etc/machine-id:/etc/machine-id \

#container can not run: amixer get Master
podman run \
 --network host \
 -e AP2HOSTNAME=qairaudio \
 -e AP2IFACE=ens18 \
 -e NO_VOLUME_MANAGEMENT=true \
 --rm -it ${imageid}

set +x


