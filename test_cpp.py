#!/usr/bin/python3

import ctypes

from csbiginteger.BigInteger import BigInteger

#if using 'csbiginteger_mono.so' implementation (default), requires 'csbiginteger_dotnet.dll' somewhere on path

def main():
    big = BigInteger()
    print('length = ', len(big))
    print('to_int = ', int(big))
    print('to_str: ', str(big))
    print('')

    big1 = BigInteger(1)
    print('length = ', len(big1))
    print('to_int = ', int(big1))
    print('to_str: ', str(big1))
    print('')

    bigM1 = BigInteger(-1)
    print('length = ', len(bigM1))
    print('to_int = ', int(bigM1))
    print('to_str: ', str(bigM1))
    print('')

    big255 = BigInteger(255)
    print('length = ', len(big255))
    print('to_int = ', int(big255))
    print('to_str: ', str(big255))
    print('')

    bigM10M = BigInteger(-1000000)
    print('length = ', len(bigM10M))
    print('to_int = ', int(bigM10M))
    print('to_str: ', str(bigM10M))
    print('')

    big4293967296 = BigInteger(4293967296)
    print('length = ', len(big4293967296))
    print('to_int = SHOULD OVERFLOW')#, big4293967296.to_int())
    print('to_str: ', str(big4293967296))
    print('')

    bigff = BigInteger(b'\xff')
    print('length = ', len(bigff))
    print('to_int = ', int(bigff))
    print('to_str: ', str(bigff))
    print('')

    big100 = BigInteger('100') # base 10 implicit
    print('length = ', len(big100))
    print('to_int = ', int(big100))
    print('to_str: ', str(big100))
    print('')

    big0001 = BigInteger('0x0001', 16) # big-endian input string
    print('length = ', len(big0001))
    print('to_int = ', int(big0001))
    print('to_str: ', str(big0001))
    print('')

    big101 = big100 + big0001 # big100 + big0001
    print('length = ', len(big101))
    print('to_int = ', int(big101))
    print('to_str: ', str(big101))
    print('')

    big99 = big100 - big0001 # big100 - big0001
    print('length = ', len(big99))
    print('to_int = ', int(big99))
    print('to_str: ', str(big99))


    return 0

if __name__ == '__main__':
    main()
