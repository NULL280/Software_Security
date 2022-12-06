As the password is first written to the file and then read for comparasion,
the solution is to write a fake password to the tmp file, so that when we
input the same fake password, we can pass the test and get the flag.

I wrote a python script that can infinitly overwrite all the "/tmp/safepassword_*"
with my fake password.

./hw2task4.py
./safepassword

Run the script first, then run safepassword, input "aabbcc", which is my
fake password. There is a chance to hit and get the flag.