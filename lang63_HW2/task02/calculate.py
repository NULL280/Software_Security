array118 = [0x47, 3, 0x5e, 5, 0x58, 0x3b, 0x1a, 0x29, 0x3d, 0xb, 0x15, 0x3e, 0x23, 0x14, 0x2b, 0x16, 0x57, 0x54, 0x61, 0x59, 1, 0x51, 10, 0x16, 0x25, 0x51, 0x3c, 0xc, 0x54, 0x38, 0, 9999]
array98 = [0 for i in range(len(array118))]
array98[0] = array118[0]
print(array98)
for i124 in range(1, len(array118)):
    for v98ATi124 in range(32, 127):
        if v98ATi124 * array98[i124 - 1] % 0x65 == array118[i124]:
            array98[i124] = v98ATi124

print(array98)
inputString = ""
for element in array98:
    inputString += chr(element)
print(inputString)
