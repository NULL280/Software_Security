sudo chown -R ubuntu18 ~
clang-9 -O0 -fsanitize=address -fno-omit-frame-pointer
cat input1_t1 | ./asan_t1_asan &> asan_t1_output