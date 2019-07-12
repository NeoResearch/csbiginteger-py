# csBigInteger.py

## csBigInteger for Python

This project is part of the [csBigInteger](https://github.com/neoresearch/csBigInteger) macro project, a C# BigInteger implementation on Python 

This project uses csBigInteger.cpp portable C++ project: https://github.com/neoresearch/csBigInteger.cpp

## How to use it?

First, you need to have `csbiginteger.so` shared library (just type `make`).

After that, this `test.py` code should work (`make run`):

```py
def main():
    big = BigInteger()
    print 'length = ', big.length()
    print 'toInt = ', big.toInt()
    return 0
```

Empty BigInteger is expected to be byte array 0x00, with size = 1 (byte) and int value zero.

```
length =  1
toInt =  0
```

## LICENSE

MIT License

2019