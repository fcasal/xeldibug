from pwn import *

def generate(assem):
	a = asm(assem)
	cshellcode = '''
	unsigned char code[] = "''' + repr(a)[1:-1] + '''";
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

generate(assem)