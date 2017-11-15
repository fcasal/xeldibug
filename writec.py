from pwn import *
import re
import ctypes

context.arch = 'amd64'
context.os = 'linux'

def generate(assem):
	a = asm(assem)[1:-1]
	a = "".join(["\\x{:02x}".format(ord(i)) for i in a])

	cshellcode = '''
	unsigned char code[] = "''' + a + '''";
	int main(void)
	{
	(*(void(*)()) code)();
	}
	'''
	open('gen.c', 'w').write(cshellcode)



assem = '''

	mov ecx,10
	l1:
	loop l1
	ret 
	
	'''

assem = '''

mov rcx, 0x1122
l1:
and rcx, 0xff00
shr rcx, 0x8
movsx rcx, cl
cmp rcx, 0x11
je l1

'''


generate(assem)