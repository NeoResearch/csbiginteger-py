# csBigInteger.py

## csBigInteger for Python 3

This project is part of the [csBigInteger](https://github.com/neoresearch/csBigInteger) macro project, a C# BigInteger implementation on Python 

This project uses csBigInteger.cpp portable C++ project: https://github.com/neoresearch/csBigInteger.cpp

## How to use it?

First, you need to have `csbiginteger.so` shared library (just type `make`).

After that, this `test.py` code should work (`make run`):

```py
from csbiginteger.BigInteger import BigInteger

def main():
    big = BigInteger()
    print('length = ', big.length())
    print('toInt = ', big.toInt())
    print('toString: ', big.toString())
    print('')

    bigM1 = BigInteger(-1)
    print('length = ', bigM1.length())
    print('toInt = ', bigM1.toInt())
    print('toString: ', bigM1.toString())
    print('')

    big4293967296 = BigInteger(4293967296)
    print('length = ', big4293967296.length())
    print('toInt = ', big4293967296.toInt())
    print('toLong = ', big4293967296.toLong())
    print('toString: ', big4293967296.toString())
    print('')

    bigff = BigInteger(b'\xff')
    print('length = ', bigff.length())
    print('toInt = ', bigff.toInt())
    print('toLong = ', bigff.toLong())
    print('toString: ', bigff.toString())
    print('')

    big100 = BigInteger('100') # base 10 implicit
    print('length = ', big100.length())
    print('toInt = ', big100.toInt())
    print('toLong = ', big100.toLong())
    print('toString: ', big100.toString())
    print('')

    big0001 = BigInteger('0x0001', 16) # big-endian input string
    print('length = ', big0001.length())
    print('toInt = ', big0001.toInt())
    print('toLong = ', big0001.toLong())
    print('toString: ', big0001.toString())
    print('')

    big101 = big100.add(big0001) # big100 + big0001
    print('length = ', big101.length())
    print('toInt = ', big101.toInt())
    print('toLong = ', big101.toLong())
    print('toString: ', big101.toString())
    print('')

    big99 = big100.sub(big0001) # big100 - big0001
    print('length = ', big99.length())
    print('toInt = ', big99.toInt())
    print('toLong = ', big99.toLong())
    print('toString: ', big99.toString())


    return 0
```

Empty BigInteger is expected to be byte array 0x00, with size = 1 (byte) and int value zero.

```
length =  1
toInt =  0
toString:  0x00

length =  1
toInt =  -1
toString:  0xff

length =  5
toInt =  -1000000
toLong =  4293967296
toString:  0x00fff0bdc0

length =  1
toInt =  -1
toLong =  -1
toString:  0xff

length =  1
toInt =  100
toLong =  100
toString:  0x64

length =  1
toInt =  1
toLong =  1
toString:  0x01

length =  1
toInt =  101
toLong =  101
toString:  0x65

length =  1
toInt =  99
toLong =  99
toString:  0x63

```

## LICENSE

MIT License

2019