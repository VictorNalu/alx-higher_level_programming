#!/usr/bin/python3
for b in range(100):
    if b == 99:
        print("{}" .format(b))
    else:
        print("{:02d}, " .format(b), end='')
