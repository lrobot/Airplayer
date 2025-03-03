#!/bin/bash

podman build --http-proxy=false .

imageid=$(podman build --http-proxy=false -q .)

podman run --rm -it ${imageid} 

