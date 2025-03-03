
podman run --rm -it \
	--http-proxy=false \
	--network host \
	--device /dev/snd \
	--device /dev/fb0 \
	-v /var/run/dbus:/var/run/dbus \
	-v /var/run/avahi-daemon/socket:/var/run/avahi-daemon/socket \
	-v /run:/run \
	dachack/uxplay \
	uxplay -d -hls -n quxplay -nh -s 1920x1080 -nohold -vs "fbdevsink device=/dev/fb0" -as "alsasink device=plughw:1,0"

# -d debug
# -hls enable video
# -name
