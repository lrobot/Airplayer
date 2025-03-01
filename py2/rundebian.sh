

podman build --http-proxy=false -f Dockerfile .
buildid=$(podman build --http-proxy=false -q -f Dockerfile .)
podman run --name airdownload --rm -it --net host -v .:/app -w /app/airplayer $buildid 

