
mpg123 -s http://maxxima.mine.nu:8000 | \
aac-enc-dabplus -a -b 64 -f raw -c 2 -r 48000 -i /dev/stdin -o /dev/stdout 2>/dev/null | \
mbuffer -q -m 100k -P 100 -s 960 | \
CRC-DabMux -m 1 -L "TuxMux"  \
-F /dev/stdin -k -b 64 -i 2 -S -L "AAC64" -C \
-O fifo:///dev/stdout |\
crc-dabmod -g2 -r3200000 | \
mbuffer -m 32m -P 25 | \
/home/mc/Dev/coinwap_uhd_full3.py

