#!/usr/bin/python

import ctypes

import csBigInteger
from csBigInteger import BigInteger

def main():
    big = BigInteger()
    print 'length = ', big.length()
    print 'toInt = ', big.toInt()

    big1 = BigInteger(1)
    print 'length = ', big1.length()
    print 'toInt = ', big1.toInt()

    bigM1 = BigInteger(-1)
    print 'length = ', bigM1.length()
    print 'toInt = ', bigM1.toInt()

    return 0

if __name__ == '__main__':
    main()


