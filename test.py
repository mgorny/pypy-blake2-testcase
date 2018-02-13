#!/usr/bin/env pypy

import io
import sys
import testmod

bufsize = 4096

with io.open('test.txt', 'wb') as f:
    data = b''
    for x in range(8):
        data += b'%d' % x
    for x in range(18):
        data += data
    f.write(data)

def sub(i):
    fpos = 0
    with io.open('test.txt', 'rb') as f:
        for j, block in enumerate(iter(lambda: f.read(bufsize), b'')):
            try:
                testmod.test(block)
            except ValueError as e:
                print("%s at top it=%d, read it=%d, fpos=%d"
                        % (e, i, j, fpos))
                print("block in python: %s" % block)
                sys.exit(1)
            fpos = f.tell()

for x in map(sub, range(100)):
    pass
