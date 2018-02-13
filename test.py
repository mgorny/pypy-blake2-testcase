#!/usr/bin/env pypy

import io
import pyblake2

bufsize = 4096
sum = '1df7d36272ba434fcca83c917352368916021ab12494dbc24a8352419b74c62948cf3cd04bd9c702ead677620e7b2ab9b0d870d2af96b745c456892e5a66d23a'

with io.open('test.txt', 'wb') as f:
    data = b''
    for x in range(14):
        data += b'%x' % x
    for x in range(18):
        data += data
    f.write(data)

def sub(i):
    cs = pyblake2.blake2b()
    with io.open('test.txt', 'rb') as f:
        for block in iter(lambda: f.read(bufsize), b''):
            cs.update(block)
    assert cs.hexdigest() == sum, i

for x in map(sub, range(10000)):
    pass
