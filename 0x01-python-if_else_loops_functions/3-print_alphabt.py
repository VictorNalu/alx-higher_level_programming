#!/usr/bin/python3
for b in range(97, 123):
    if chr(b) in ('q', 'e'):
        continue
    print("{}" .format(chr(b)), end='')
