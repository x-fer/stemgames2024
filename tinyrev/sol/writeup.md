# TinyRev

Description: Strings won't help you here.

Hint (if we want to do those): take a look at binary patching

## Writeup
Open up the binary in your decompiler of choice. Notice it's doing some MD5 stuff to your input, and checking it against a precomputed hash. 

Reverse the if condition on the correct/wrong check (change JNZ at 0x10122f to a JZ). Input any string, get the flag.

It's also possible to extract the two arrays secure_cipher() reads from and xor them manually to get the flag.

Learn more:
https://vickieli.dev/binary%20exploitation/intro-to-binary-patching/
https://www.felixcloutier.com/x86/jcc

