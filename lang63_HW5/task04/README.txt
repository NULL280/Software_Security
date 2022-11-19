Stack:    Canary found
    cannot do buffer overflow
NX:       NX enabled
    cannot run binary on stack
PIE:      PIE enabled
    return address is unknown

solution: trigger the sig_handler (print the flag) by floating-point overflow

a = -2147483648
b = -1
|mini_int| = |max_int| + 1
overflow when mini_int / -1
get the flag