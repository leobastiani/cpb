#!python3
#encoding=utf-8
from __future__ import print_function, division

import sys
import pyperclip
import time

def main():
    history = []
    def out(*args):
        history.append(*args)
        print(*args)

    cpb = pyperclip.paste()
    if cpb != '':
        out(cpb)

    try:
        while 1:
            time.sleep(0.1)
            newCpb = pyperclip.paste()
            if newCpb != cpb:
                out(newCpb)
                cpb = newCpb
    except KeyboardInterrupt:
        pyperclip.copy('\n'.join(history))

if __name__ == '__main__':
    main()
