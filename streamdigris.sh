#!/bin/sh

#mplayer -ao jack:name=maxxima http://maxxima.mine.nu:8000 &

for i in 1 2 3 4 5 6 7 8 9 10 11
do
jack-stdout $i:out_0 $i:out_1 |\
aac-enc-dabplus -a -b 80 -f raw -c 2 -r 32000 -i /dev/stdin -o /dev/stdout 2>/dev/null | \
mbuffer -q -m 100k -P 100 -s 960 > /home/mc/Dev/fifo/$i.ff &
#echo "$i".ff
done


