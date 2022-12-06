Part1: dictionary file
by reversing the fuzz3 through ghidra, the words for dictionary file should be name1 = "UPPR" "LOWR" "ENDD"

# input_dir: with aflinput
~/Apps/afl-2.52b/afl-fuzz -Q -i input -o output -x dict1 ./fuzz3

The ALF uses this dictionary file found the first crash in 3 minute

Part2: inpujt1_t3
find crash in output/crashes
I found 1 and it does crash fuzz3

Part3: input1minimized_t3
~/Apps/afl-2.52b/afl-tmin -Q -i input1_t3 -o input1minimized_t3 ./fuzz3