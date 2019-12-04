#!python3
#encoding=utf-8
from __future__ import print_function, division

import sys
import pyperclip
import time

tudo = []
def out(*args):
    tudo.append(*args)
    print(*args)

cpb = pyperclip.paste()
if cpb != '':
    out(cpb)

try:
    while 1:
        time.sleep(0.5)
        newCpb = pyperclip.paste()
        if newCpb != cpb:
            out(newCpb)
            cpb = newCpb
except KeyboardInterrupt:
    pyperclip.copy('\n'.join(tudo))
