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

    big255 = BigInteger(255)
    print 'length = ', big255.length()
    print 'toInt = ', big255.toInt()

    bigM10M = BigInteger(-1000000)
    print 'length = ', bigM10M.length()
    print 'toInt = ', bigM10M.toInt()
    print 'toLong = ', bigM10M.toLong()

    big4293967296 = BigInteger(4293967296)
    print 'length = ', big4293967296.length()
    print 'toInt = ', big4293967296.toInt()
    print 'toLong = ', big4293967296.toLong()

    return 0

if __name__ == '__main__':
    main()


