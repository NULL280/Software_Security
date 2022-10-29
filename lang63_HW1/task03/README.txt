The echo_as_a_service binary use system() to run cmd. The goal is to let it
run cat flag.txt

Here is my command:
./echo_as_a_service "\";cat flag.txt;echo \""

"" outside to put everything as a whole string.
\" to have " to part with " after echo
;echo \" to deal with second "

flag: xkjbqHVBhwmXaoxJmKtmmchHfHTpiQ