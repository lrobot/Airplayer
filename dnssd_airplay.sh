

# dns-sd -L "家庭活动室 Apple TV" _airplay._tcp
# dns-sd -B _raop._tcp
# dns-sd -B _airplay._tcp

dnssd_airplay() {
TEMPFILE=`mktemp`
cat <<EOF > ${TEMPFILE}
send-keys 'dns-sd -R "MythTV" _airplay._tcp local 7000 "deviceid=58:55:CA:12:34:56" "features=0x39f7" "model=AppleTV2,1" "srcvers=130.14"' 'C-m'
splitw -h
send-keys 'dns-sd -R 5855CA123456@MythTV _raop._tcp local 49152 "da=true" "vs=115.2" "md=0,1,2" "txtvers=1" "vn=3" "pw=false" "sr=44100" "ss=16" "ch=2" "cn=0,1" "et=0,1" "ek=1" "sv=false" "sm=false" "tp=UDP"' 'C-m'
attach
EOF
tmux new\; source-file $TEMPFILE
rm -f ${TEMPFILE}
}

dnssd_airplay