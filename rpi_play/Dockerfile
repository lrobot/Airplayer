FROM lrobot/debian:bookworm as builder
RUN apt-get update
RUN apt-get install -yy cmake libavahi-compat-libdnssd-dev libplist-dev libssl-dev \
libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev gstreamer1.0-libav \
gstreamer1.0-vaapi gstreamer1.0-plugins-bad
COPY . /build
RUN mkdir -p /build/out
WORKDIR /build/out
RUN cmake ..
RUN make
CMD ["/build/out/rpiplay"]

#FROM lrobot/debian:bookworm as runner
#RUN apt-get update
#COPY --from=builder /build/out/rpiplay  /app/rpiplay


