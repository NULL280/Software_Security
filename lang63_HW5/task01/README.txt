Stack:    Canary found
    cannot buffer overflow
NX:       NX enabled
    cannot run shell code on stack
PIE:      No PIE (0x400000)
    return address is known

have to use rop chain

Solution:
get ROP shellcode:
ROPgadget --ropchain --binary "binary path" > "output path"


sent (unsigned short) minimun short + 1

overwrite the function pointer with return address

add the ROP chain after it

code for doing thins in hw5task1.py