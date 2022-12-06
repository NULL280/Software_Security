task02 readme

get the gof table index by elf.got['puts']:
# 6295320

get the libc system(), puts() location, use them to calculate offset value

read at 6295320 to get puts address

calcuate system address use puts address and offset

write system address at 6295320

type 3 (echo)