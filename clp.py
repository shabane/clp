#!/usr/bin/env python3

import sys
import pyperclip
import os

def help():
    print("""
        this is help
    """)
    sys.exit(0)


def copyFromFile(paths: list):
    x = ''
    if paths:
        for path in paths:
            if not os.path.exists(path):
                print(f'fetal: path {path} does not exist')
                sys.exit(1)
            with open(path, mode='r') as fli:
                if tmp := fli.read():
                    if tmp.strip() != '':
                        x += tmp
                    else:
                        print(f'warning: file {path} was empty')

    pyperclip.copy(x)


def copyFromArg() -> bool:
    """
    copy all args whitch user pass to clp
    :return: bool
    """
    x = ''
    for i in sys.argv[1:]:
        x += i
    pyperclip.copy(x)
    return True

def copyFromPipe():
    if (x := sys.stdin.read()):
        if x.strip() != '':
            pyperclip.copy(str(x))
            return True
        else:
            return False
            print('fetal: input is empty')
            sys.exit(1)
    else:
        return False
        print('fetal: no input given')
        sys.exit(1)


if len(sys.argv) >= 2:
    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        help()
    elif len(sys.argv) >= 3:
        if sys.argv[1] == '-i' or sys.argv[1] == '--input-file':
            if sys.argv[2:]:
                copyFromFile(sys.argv[2:])
            else:
                print('fetal: no input file given')
                sys.exit(1)
    else:
        copyFromArg()
else:
    copyFromPipe()
