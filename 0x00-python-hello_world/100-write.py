#!/usr/bin/python3
import sys
feed = "and that piece of art is useful - Dora Korpar, 2015-10-19"
#writes to stderr using sys.stderr.write
sys.stderr.write(feed + '\n')
# Exits with status code 1
sys.exit(1)
