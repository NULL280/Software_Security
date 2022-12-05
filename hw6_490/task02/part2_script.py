from pwn import*
context(arch="amd64", os="linux")
p=process('./asan_t2_asan')
p.sendline(b'8000')
payload=b'8000'
payload+=b"\n"
for i in range(1,8001):
    payload+=b'7777777'
    payload+=b"\n"
    p.sendline(b'7777777')
print(p.recv())
payload+=b'1'
payload+=b"\n"
p.sendline(b'1')
f=open("input2_t2", "wb")
f.write(payload)
f.close()
print(p.recv())