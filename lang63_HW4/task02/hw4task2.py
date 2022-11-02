from pwn import *
elf = ELF("./yougotme")
print(elf.got("puts"))