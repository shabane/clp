#!/usr/bin/env python3

import sys
import pyperclip


def help():
    print("""
        this is help
    """)
    sys.exit(0)


if len(sys.argv) > 1:

    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        help()

    x = ''
    for i in sys.argv[1:]:
        x += i
        print(x)
    pyperclip.copy(x)
else:
    if(x:= sys.stdin.read()):
        if x.strip() != '':
            pyperclip.copy(x)
        else:
            print('fetal: input is empty')
            sys.exit(1)
    else:
        print('fetal: no input given')
        sys.exit(1)
