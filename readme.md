# clp

sometimes we need to **copy result of some program to clipboard**. or we need to
copy a text file to clipboard. this simple program will help you on that.


## tabebl of content

> - [features](#features)
> - [usage](#usage)
> - [examples](#examples)
> - [preview](#preview)
> - [installation](#installation)
> - [license](#license)


## features

1. you can *pipe* any text base result of a program.
2. you can pass a *bunch of file paths* to copy their content to clipboard.
3. you can pass *any text*
4. you can run program without any switchs and agrs, this will copy your text from the *prompt*.


## usage

- to see the help enter `clp -h`

```bash
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
```

## examples

1. pipe

```bash
    $ ls /var | clp 
```

2. from file

```bash
    $ clp -i /var/log/syslog
```

3. pass texts

```bash
    $ clp this text will copy to clipboard as well as other way
    
    # warning: no input was given, consider args as input text
```

4. prompt

```bash
    $ clp
```


## preview

> from input file
> ![input](https://bit-orbit.github.io/CDN/files/images/input.gif)

> pipe result to clp
> ![pipe](https://bit-orbit.github.io/CDN/files/images/pipe.gif)

> type a text and then copy it to clipboard
> ![promt](https://bit-orbit.github.io/CDN/files/images/promt.gif)

> consider args as text to copy
> ![arg](https://bit-orbit.github.io/CDN/files/images/arg.gif)


## installation

install dependencies

```bash
  $ pip3 install pyperclip

  # if you dont have the pip3, install it first.
```

download the program

```bash
  $ cd /tmp && wget 'https://raw.githubusercontent.com/shabane/clp/master/clp.py'
```

add the clp to user programs

```bash
  $ cp clp.py ~/.local/bin/clp
```

add execute permission to clp

```bash
    $ chmod +x ~/.local/bin/clp
```

test the installation

```bash
    $ clp -h
```


## license

- [GPL](https://github.com/shabane/clp/blob/master/license)
- work on my machine
