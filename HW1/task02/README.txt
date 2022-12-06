The my_cat binary can read the file, but doesnot allow the path contain "flag"
chars.

To avoid this, I creat a symbolic link with name "123":
ln -s ./flag.txt 123

Then run my_cat with this link:
./my_cat 123

And get the flag:
flag: weBeKLORyIGHHIEWQDlXeamTnznnGI