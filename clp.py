#!/usr/bin/env python3

import sys
import pyperclip
import os

def help():
    print("""
    DESCRIOTOON
      copy stdin or file content to clipboard.
      in order to copy the resutl of one program to clipboard you should
      pipe the result to clp.
      
      if you do not use switches, the stdin will copy to clipboard
      
    OPTIONS
      -h, --help
        display this help and exit.
      
      -i, --input-file
        read the path file and copy the file content to clipboard.

    EXAMPLES
        Example I
        ls /var | clp 
        clp will copy the list of files cite in the /var directory
                
        Example II 
        clp -i /var/log/syslog
        clp will read the content of the /var/log/syslog file and then copy that content to clipboard        
        
        Example III
        clp 'this text will copy to clipboard as well as other way'
        
        Example IV
        clp
        this will get your text from the prompt. you should press ctrl+D to done the writing.
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
            copyFromFile(sys.argv[2:])
    else:
        print('warning: no input was given, consider args as input text')
        copyFromArg()
else:
    copyFromPipe()
