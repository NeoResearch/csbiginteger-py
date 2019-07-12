#!/usr/bin/python

import ctypes

import csBigInteger
from csBigInteger import BigInteger

def main():
    big = BigInteger()
    print 'length = ', big.length()
    print 'toInt = ', big.toInt()
    return 0

if __name__ == '__main__':
    main()


