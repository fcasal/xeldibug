#!/bin/sh

python writec.py
gcc gen.c -fno-stack-protector -z execstack -o shellcode
rm ./gen.c
chmod +x shellcode
echo $'use this:\n\n >>>>>>>>>>     aaa; s main; db `pdf~call[0]`; dc\n\n'
r2 -d shellcode