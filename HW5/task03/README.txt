Stack:    No canary found
    possible for stack overflow
NX:       NX enabled
    cannot run shell code on stack
PIE:      PIE enabled
    return address unknown

use format string attacks
rsi: %p, rdx: %p, rcx: %p, r8: %p, r9: %p, stack: %p %p

#print stack from rsp, each time 8 bytes, lower address at right

Solution:
get printf from rdx (%2$p)

get libc system and printf address, cal difference

system address = printf + difference

overflow the secound input, with system() address and /bin/sh

code to do these in hw5task3.py