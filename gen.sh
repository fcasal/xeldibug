#!/bin/sh

python writec.py
gcc gen.c -fno-stack-protector -z execstack -o shellcode
rm ./gen.c
chmod +x shellcode
clear
echo '\n\n****************************************'
echo '>>> breakpoint is at the shellcode call'
echo '>>> use s to step forward           '
echo '****************************************\n\n'

r2 -d shellcode -c 'aaa; s main; db `pdf~call[0]`; dc'
