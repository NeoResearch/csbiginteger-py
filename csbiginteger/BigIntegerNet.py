#!/usr/bin/python3


from csbiginteger.BigInteger import BigInteger

from functools import total_ordering

# requires: pip install msl-loadlib pycparser pythonnet
from msl.loadlib import LoadLibrary

# remember to execute first: cd csbiginteger/dotnet && dotnet build -c Release
net = LoadLibrary('csbiginteger/dotnet/bin/Release/netstandard2.0/csbiginteger.dll', 'net')

biglib = net.lib.csbiglib.BigIntegerLib()

z = biglib.zero()
print(bytearray(z.ToByteArray()))

m1 = biglib.from_int32(-1)
print(bytearray(m1.ToByteArray()))

i255 = biglib.from_int32(255)
print(bytearray(i255.ToByteArray()))

b2 = biglib.from_bytes(bytearray(i255.ToByteArray()))
print(biglib.to_int32(b2))

b3 = biglib.from_string("0xff", 16)
print(biglib.to_int32(b3))

print(biglib.to_string(b3, 16))
print(biglib.to_string(b3, 10))
print(bytearray(biglib.to_bytes(b3)))

@total_ordering
class BigIntegerNet(BigInteger):
    # param may be: int, bytearray, bytes, string (parsed with base)
    # bytes and bytearray should be received in little-endian format (same as to_bytearray() returns)
    def __init__(self, param=0, base=10):
        if type(param) is int:
            param = str(param)  # convert to base-10 integer
            base = 10  # force base 10
        if type(param) is bytearray:
            param = bytes(param)  # bytearray to bytes
        if type(param) is bytes:
            self._big = biglib.from_bytes(bytearray(param))
        if type(param) is str:
            self._big = biglib.from_string(param, base)


    # returns value in signed int32 limit (or exception)
    def to_int(self):
        return biglib.to_int32(self._big)

    def to_long(self):
        return biglib.to_int64(self._big)

    # bytearray is returned in little-endian format
    def to_bytearray(self):
        return bytearray(biglib.to_bytes(self._big))

    def to_str(self, base=16):
        return str(biglib.to_string(self._big, base))

    def add(self, other):
        if type(other) is int:
            other = BigIntegerNet(other)
        
        big3 = BigIntegerNet()
        big3._big = self._big.Add(self._big, other._big)
        return big3

    def sub(self, other):
        if type(other) is int:
            other = BigIntegerNet(other)
        
        big3 = BigIntegerNet()
        big3._big = self._big.Subtract(self._big, other._big)
        return big3

    def mul(self, other):
        if type(other) is int:
            other = BigIntegerNet(other)
        
        big3 = BigIntegerNet()
        big3._big = self._big.Multiply(self._big, other._big)
        return big3

    def div(self, other):
        if type(other) is int:
            other = BigIntegerNet(other)
        
        big3 = BigIntegerNet()
        big3._big = self._big.Divide(self._big, other._big)
        return big3


    def mod(self, other):
        if type(other) is int:
            other = BigIntegerNet(other)
        
        big3 = BigIntegerNet()
        big3._big = self._big.DivRem(self._big, other._big)
        return big3


    def shl(self, other):
        if type(other) is int:
            other = BigIntegerNet(other)
        
        big3 = BigIntegerNet()
        big3._big = self._big.op_LeftShift(other._big)
        return big3


    def shr(self, other):
        if type(other) is int:
            other = BigIntegerNet(other)
        
        big3 = BigIntegerNet()
        big3._big = self._big.op_RightShift(other._big)
        return big3

    def eq(self, other):
        if type(other) is int:
            other = BigIntegerNet(other)
        
        return self._big.op_Equality(other._big)


    def lt(self, other):
        if type(other) is int:
            other = BigIntegerNet(other)
        
        return self._big.op_LessThan(other._big)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.to_str(10)

    def __len__(self):
        return len(self.to_bytearray())

    # ---------
    # operators
    # ---------
    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.sub(other)

    def __mul__(self, other):
        return self.mul(other)

    # note that python usually follows 'pure floor' operation here, on a // b => floor(a/b)
    # example: -5 // 2 => -3 (standard int on python)
    # however, this library follows hardware-standard (from c/c++/java/fortran), of truncating positive or negative
    # so, here: BigInteger(-5) // BigInteger(2) => -2 ("rounding" up, not down)
    # floordiv is thus not a good name, since it's only floor for positive division, but ceil for negative, but that's what we have :)
    def __floordiv__(self, other):
        return self.div(other)

    # truediv does not exist (using a // b)
    def __truediv__(self, other):
        return self.div(other)

    def __mod__(self, other):
        return self.mod(other)

    def __rshift__(self, other):
        return self.shr(other)

    def __lshift__(self, other):
        return self.shl(other)

    # comparisons
    # -----------
    def __eq__(self, other):
        return self.eq(other)

    # def __gt__(self, other):
    #    return self.gt(other)

    def __lt__(self, other):
        return self.lt(other)
