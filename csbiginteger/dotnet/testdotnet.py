
#!/usr/bin/python3

from msl.loadlib import LoadLibrary

net = LoadLibrary('./bin/Release/netstandard2.0/csbiginteger.dll', 'net')

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
