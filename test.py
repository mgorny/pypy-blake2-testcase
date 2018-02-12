#!/usr/bin/env pypy

import io
import multiprocessing
import pyblake2

bufsize = 4096
sum = 'ccefcd101b08863339602f7fdf2edd1d77ef05a970c36dbd7a560d33f957f81b15cfcac10114f8fca0d7c318b6aaa294220e3fcf4f88e6e3bd7840f121ff3b65'

def sub(i):
    cs = pyblake2.blake2b()
    with io.open('test.txt', 'rb') as f:
        for block in iter(lambda: f.read(bufsize), b''):
            cs.update(block)
    assert cs.hexdigest() == sum

def gen():
    for i in xrange(100000):
        yield i

p = multiprocessing.Pool()
for x in p.imap_unordered(sub, gen(), chunksize=32):
    pass
p.close()
