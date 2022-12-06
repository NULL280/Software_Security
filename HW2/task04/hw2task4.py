#!/usr/bin/env python3
import glob
i = 0
while 1 < 10:
    fileList = glob.glob('/tmp/safe*')
    for file in fileList:
        fp = open(file, "w")
        fp.write("aabbcc")
        fp.close()
