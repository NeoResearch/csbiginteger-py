# csBigInteger.py

## csBigInteger for Python 3

This project is part of the [csBigInteger](https://github.com/neoresearch/csBigInteger) macro project, a C# BigInteger implementation on Python 

This project uses csBigInteger.cpp portable C++ project: https://github.com/neoresearch/csBigInteger.cpp

### build dependencies

First, you need to have `csbiginteger.so` shared library (just type `make`).

**Important:** Remember to clone `csBigInteger.cpp` portable submodule (`git clone --recursive`).

## How to use it?

Try `test.py` code, it should work! (or just type `make run`):

```py
from csbiginteger.BigInteger import BigInteger

def main():
    big = BigInteger()
    print('length = ', big.length())
    print('to_int = ', big.to_int())
    print('to_str: ', big.to_str())
    print('')

    bigM1 = BigInteger(-1)
    print('length = ', bigM1.length())
    print('to_int = ', bigM1.to_int())
    print('to_str: ', bigM1.to_str())
    print('')

    big4293967296 = BigInteger(4293967296)
    print('length = ', big4293967296.length())
    print('to_int = ', big4293967296.to_int())
    print('to_long = ', big4293967296.to_long())
    print('to_str: ', big4293967296.to_str())
    print('')

    bigff = BigInteger(b'\xff')
    print('length = ', bigff.length())
    print('to_int = ', bigff.to_int())
    print('to_long = ', bigff.to_long())
    print('to_str: ', bigff.to_str())
    print('')

    big100 = BigInteger('100') # base 10 implicit
    print('length = ', big100.length())
    print('to_int = ', big100.to_int())
    print('to_long = ', big100.to_long())
    print('to_str: ', big100.to_str())
    print('')

    big0001 = BigInteger('0x0001', 16) # big-endian input string
    print('length = ', big0001.length())
    print('to_int = ', big0001.to_int())
    print('to_long = ', big0001.to_long())
    print('to_str: ', big0001.to_str())
    print('')

    big101 = big100.add(big0001) # big100 + big0001
    print('length = ', big101.length())
    print('to_int = ', big101.to_int())
    print('to_long = ', big101.to_long())
    print('to_str: ', big101.to_str())
    print('')

    big99 = big100.sub(big0001) # big100 - big0001
    print('length = ', big99.length())
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