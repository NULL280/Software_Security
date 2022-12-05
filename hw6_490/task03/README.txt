./afl-2.52b/afl-fuzz
-Q
-i (input folder)
-o (output folde)
-x (dictionary file)
last argument is the binary
total crashes : 6 (4 unique)

./afl-2.52b/afl-tmin -Q -i input1_t3 -o input1minimized_t3 ./fuzz3
cat input1minimized_t3 | ./fuzz3