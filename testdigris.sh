
#mpg123 -s http://maxxima.mine.nu:8000 | \
#aac-enc-dabplus -a -b 64 -f raw -c 2 -r 48000 -i /dev/stdin -o /dev/stdout 2>/dev/null | \
#mbuffer -q -m 100k -P 100 -s 960 | \
CRC-DabMux -m 1 -L "DIG2 F03"  \
-F /home/mc/Dev/fifo/1.ff -k -b 80 -i 1 -S -i 0x3EB1 -L "Global FM" -C \
-F /home/mc/Dev/fifo/2.ff -k -b 80 -i 2 -S -i 0x3EB0 -L "Maxxima" -C \
-F /home/mc/Dev/fifo/3.ff -k -b 80 -i 3 -S -i 0x3EB3 -L "Frequence Banane" -C \
-F /home/mc/Dev/fifo/4.ff -k -b 80 -i 4 -S -i 0x3EB2 -L "La Fabrik" -C \
-F /home/mc/Dev/fifo/5.ff -k -b 80 -i 5 -S -i 0x3E19 -L "Radio Cite" -C \
-F /home/mc/Dev/fifo/6.ff -k -b 80 -i 6 -S -i 0x3EA4 -L "Open Broadcast" -C \
-F /home/mc/Dev/fifo/7.ff -k -b 80 -i 7 -S -i 0x3EA7 -L "Radio Ouistiti" -C \
-F /home/mc/Dev/fifo/8.ff -k -b 80 -i 8 -S -i 0x3EB4 -L "Backstage Radio" -C \
-F /home/mc/Dev/fifo/9.ff -k -b 80 -i 9 -S -i 0x3EB4 -L "WRS New" -C \
-F /home/mc/Dev/fifo/10.ff -k -b 80 -i 10 -S -i 0x3EA9 -L "Radio 74" -C \
-F /home/mc/Dev/fifo/11.ff -k -b 80 -i 11 -S -i 0x3EA8 -L "Spoon Radio" -C \
-O fifo:///dev/stdout |\
crc-dabmod -g2 -r3200000 | \
mbuffer -m 32m -P 25 | \
/home/mc/Dev/coinwap_uhd_full3.py

