#!/usr/bin/env python3
from pwn import *

elf = ELF("./yougotme")
print(elf.got['puts'])
print(elf.got['system'])