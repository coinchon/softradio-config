
mplayer -ao jack:name=maxxima http://maxxima.mine.nu:8000 &

jack-stdout maxxima:out_0 maxxima:out_1 |\
aac-enc-dabplus -a -b 64 -f raw -c 2 -r 48000 -i /dev/stdin -o /dev/stdout 2>/dev/null | \
mbuffer -q -m 100k -P 100 -s 960 >/home/mc/Dev/fifo/1.ff



