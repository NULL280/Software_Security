from pwn import *
context(arch="amd64", os="linux")
pr = process("./babyshell")
print(pr.recvline())