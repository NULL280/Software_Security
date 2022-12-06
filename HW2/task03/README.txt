By reverse engineering the binary, I found the 2 functions are on the same
part of stack. The admin checker check a variable which is not initialized.

By initialized that variable to 0x1337, the code will pase the test and
read the flag.

To input the 0x13 ascii char, I wrote a python script: hw2task3.py

./hw2task3.py | ./time_management