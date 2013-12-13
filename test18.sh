
#mpg123 -s http://maxxima.mine.nu:8000 | \
#aac-enc-dabplus -a -b 64 -f raw -c 2 -r 48000 -i /dev/stdin -o /dev/stdout 2>/dev/null | \
#mbuffer -q -m 100k -P 100 -s 960 | \
CRC-DabMux -m 1 -L "TuxMux"  \
-F /home/mc/Dev/fifo/1.ff -k -b 64 -i 1 -S -L "AAC1" -C \
-F /home/mc/Dev/fifo/2.ff -k -b 64 -i 2 -S -L "AAC2" -C \
-F /home/mc/Dev/fifo/3.ff -k -b 64 -i 3 -S -L "AAC3" -C \
-F /home/mc/Dev/fifo/4.ff -k -b 64 -i 4 -S -L "AAC4" -C \
-F /home/mc/Dev/fifo/5.ff -k -b 64 -i 5 -S -L "AAC5" -C \
-F /home/mc/Dev/fifo/6.ff -k -b 64 -i 6 -S -L "AAC6" -C \
-F /home/mc/Dev/fifo/7.ff -k -b 64 -i 7 -S -L "AAC7" -C \
-F /home/mc/Dev/fifo/8.ff -k -b 64 -i 8 -S -L "AAC8" -C \
-F /home/mc/Dev/fifo/9.ff -k -b 64 -i 9 -S -L "AAC9" -C \
-F /home/mc/Dev/fifo/10.ff -k -b 64 -i 10 -S -L "AAC10" -C \
-F /home/mc/Dev/fifo/11.ff -k -b 64 -i 11 -S -L "AAC11" -C \
-F /home/mc/Dev/fifo/12.ff -k -b 64 -i 12 -S -L "AAC12" -C \
-F /home/mc/Dev/fifo/13.ff -k -b 64 -i 13 -S -L "AAC13" -C \
-F /home/mc/Dev/fifo/14.ff -k -b 64 -i 14 -S -L "AAC14" -C \
-F /home/mc/Dev/fifo/15.ff -k -b 64 -i 15 -S -L "AAC15" -C \
-F /home/mc/Dev/fifo/16.ff -k -b 64 -i 16 -S -L "AAC16" -C \
-F /home/mc/Dev/fifo/17.ff -k -b 64 -i 17 -S -L "AAC17" -C \
-F /home/mc/Dev/fifo/18.ff -k -b 64 -i 18 -S -L "AAC18" -C \
-O fifo:///dev/stdout |\
crc-dabmod -g2 -r3200000 | \
mbuffer -m 32m -P 25 | \
/home/mc/Dev/coinwap_uhd_full3.py

