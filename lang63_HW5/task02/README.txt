host: set_05_miningx_lang63_1 (netcat)
flag.txt: /home/task02/flag.txt

Stack:    Canary found
NX:       NX disabled
PIE:      No PIE (0x400000)
RWX:      Has RWX segments

NX, PIE disabled:
can do shellcode

Canary found:
bypass canary, by overwrite the canary 1 byte at a time