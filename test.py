#!/usr/bin/python3

import ctypes

#import csbiginteger.csbiginteger
#from csbiginteger import hello

#import csbiginteger
from csbiginteger.BigInteger import BigInteger


def main():
    big = BigInteger()
    print('length = ', big.length())
    print('toInt = ', big.toInt())
    print('toString: ', big.toString())
    print('')

    big1 = BigInteger(1)
    print('length = ', big1.length())
    print('toInt = ', big1.toInt())
    print('toString: ', big1.toString())
    print('')

    bigM1 = BigInteger(-1)
    print('length = ', bigM1.length())
    print('toInt = ', bigM1.toInt())
    print('toString: ', bigM1.toString())
    print('')

    big255 = BigInteger(255)
    print('length = ', big255.length())
    print('toInt = ', big255.toInt())
    print('toString: ', big255.toString())
    print('')

    bigM10M = BigInteger(-1000000)
    print('length = ', bigM10M.length())
    print('toInt = ', bigM10M.toInt())
    print('toLong = ', bigM10M.toLong())
    print('toString: ', bigM10M.toString())
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

    return 0

if __name__ == '__main__':
    main()


