#!/bin/bash

set -o nounset
asmfile=$1

# creates a header file that will be prepended to the hex files created
echo "v2.0 raw" > header.tmp

# .text starts at address 0x0000
# .data starts at address 0x2000

# runs mars on the assembly file
# outputs the text segment in $asmfile.text.hex
java -jar mars.jar a dump .text HexText text_t.hex nc mc CompactTextAtZero $asmfile
cat header.tmp text_t.hex > $asmfile.text.hex

# runs mars on the assembly file
# outputs the memory contents of data segment in $asmfile.data.hex
java -jar mars.jar a dump .data HexText data_t.hex nc mc CompactTextAtZero $asmfile

# filler before .data segment
echo 00000000 | awk '{for(i=0;i<8192;i++)print}' > filler_t.hex

cat header.tmp filler_t.hex data_t.hex > $asmfile.data.hex

rm text_t.hex
rm data_t.hex
rm filler_t.hex
rm header.tmp
