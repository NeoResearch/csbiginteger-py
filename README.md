# csBigInteger.py

## csBigInteger for Python 3

This project is part of the [csBigInteger](https://github.com/neoresearch/csBigInteger) macro project, a C# BigInteger implementation on Python 

This project uses csBigInteger.cpp portable C++ project: https://github.com/neoresearch/csBigInteger.cpp

### build dependencies

First, you need to have `csbiginteger.so` shared library (just type `make vendor`). 
This command will also install debian/ubuntu dependency on GNU GMP library (from csBigInteger.cpp project): `sudo apt install libgmp-dev`.

Don't worry, we are already shipping a `linux x86-64` library for you (no default windows build yet.. help is appreciated!).

**Important:** Remember to clone `csBigInteger.cpp` portable submodule (`git clone --recursive` or `git pull --recurse-submodules`).

## How to use it?

Try `test.py` code, it should work! (or just type `make run`):

```py
from csbiginteger.BigInteger import BigInteger

def main():
    big = BigInteger()
    print('length = ', len(big))
    print('to_int = ', big.to_int())
    print('to_str: ', big.to_str())
    print('')

    bigM1 = BigInteger(-1)
    print('length = ', len(bigM1))
    print('to_int = ', bigM1.to_int())
    print('to_str: ', bigM1.to_str())
    print('')

    big4293967296 = BigInteger(4293967296)
    print('length = ', len(big4293967296))
    print('to_int = ', big4293967296.to_int())
    print('to_long = ', big4293967296.to_long())
    print('to_str: ', big4293967296.to_str())
    print('')

    bigff = BigInteger(b'\xff')
    print('length = ', len(bigff))
    print('to_int = ', bigff.to_int())
    print('to_long = ', bigff.to_long())
    print('to_str: ', bigff.to_str())
    print('')

    big100 = BigInteger('100') # base 10 implicit
    print('length = ', len(big100))
    print('to_int = ', big100.to_int())
    print('to_long = ', big100.to_long())
    print('to_str: ', big100.to_str())
    print('')

    big0001 = BigInteger('0x0001', 16) # big-endian input string
    print('length = ', len(big0001))
    print('to_int = ', big0001.to_int())
    print('to_long = ', big0001.to_long())
    print('to_str: ', big0001.to_str())
    print('')

    big101 = big100.add(big0001) # big100 + big0001
    print('length = ', len(big101))
    print('to_int = ', big101.to_int())
    print('to_long = ', big101.to_long())
    print('to_str: ', big101.to_str())
    print('')

    big99 = big100.sub(big0001) # big100 - big0001
    print('length = ', len(big99))
    print('to_int = ', big99.to_int())
    print('to_long = ', big99.to_long())
    print('to_str: ', big99.to_str())


    return 0
```

Empty BigInteger is expected to be byte array 0x00, with size = 1 (byte) and int value zero.

```
length =  1
to_int =  0
to_str:  0x00

length =  1
to_int =  -1
to_str:  0xff

length =  5
to_int =  -1000000
to_long =  4293967296
to_str:  0x00fff0bdc0

length =  1
to_int =  -1
to_long =  -1
to_str:  0xff

length =  1
to_int =  100
to_long =  100
to_str:  0x64

length =  1
to_int =  1
to_long =  1
to_str:  0x01

length =  1
to_int =  101
to_long =  101
to_str:  0x65

length =  1
to_int =  99
to_long =  99
to_str:  0x63

```

## LICENSE

MIT License

2019
