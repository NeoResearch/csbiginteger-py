#!/usr/bin/python3

import ctypes

#import csbiginteger.csbiginteger
#from csbiginteger import hello

#import csbiginteger
from csbiginteger.BigInteger import BigInteger

# or use dotnet version
from csbiginteger.BigIntegerNet import BigIntegerNet


def main():
    big = BigIntegerNet()
    print('length = ', len(big))
    print('to_int = ', big.to_int())
    print('to_str: ', big.to_str())
    print('')

    big1 = BigIntegerNet(1)
    print('length = ', len(big1))
    print('to_int = ', big1.to_int())
    print('to_str: ', big1.to_str())
    print('')

    bigM1 = BigIntegerNet(-1)
    print('length = ', len(bigM1))
    print('to_int = ', bigM1.to_int())
    print('to_str: ', bigM1.to_str())
    print('')

    big255 = BigIntegerNet(255)
    print('length = ', len(big255))
    print('to_int = ', big255.to_int())
    print('to_str: ', big255.to_str())
    print('')

    bigM10M = BigIntegerNet(-1000000)
    print('length = ', len(bigM10M))
    print('to_int = ', bigM10M.to_int())
    print('to_long = ', bigM10M.to_long())
    print('to_str: ', bigM10M.to_str())
    print('')

    big4293967296 = BigIntegerNet(4293967296)
    print('length = ', len(big4293967296))
    print('to_int = OVERFLOW')#, big4293967296.to_int())
    print('to_long = ', big4293967296.to_long())
    print('to_str: ', big4293967296.to_str())
    print('')

    bigff = BigIntegerNet(b'\xff')
    print('length = ', len(bigff))
    print('to_int = ', bigff.to_int())
    print('to_long = ', bigff.to_long())
    print('to_str: ', bigff.to_str())
    print('')

    big100 = BigIntegerNet('100') # base 10 implicit
    print('length = ', len(big100))
    print('to_int = ', big100.to_int())
    print('to_long = ', big100.to_long())
    print('to_str: ', big100.to_str())
    print('')

    big0001 = BigIntegerNet('0x0001', 16) # big-endian input string
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

if __name__ == '__main__':
    main()


