Part1: input1_t1
use script build_input1_t1.py to build input1_t1
cat input1_t1 | ./asan_t1

Part2: asan_t1_asan
clang-9 -O0 -fsanitize=address -fno-omit-frame-pointer ./asan_t1.c -o asan_t1_asan

Part3: asan_t1_output
input1_t1 does not exploit asan_t1_asan
cat input1_t1 | ./asan_t1_asan &> asan_t1_output