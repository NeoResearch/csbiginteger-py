#!/usr/bin/python3

import ctypes
from functools import total_ordering
from typing import TypeVar, Type
T = TypeVar('T', bound='BigInteger')

csbiginteger_lib = ctypes.cdll.LoadLibrary('csbiginteger/csbiginteger.so')
# csbiginteger_to_string (byte* vb, int sz_vb, int base, char* sr, int sz_sr) -> bool
csbiginteger_lib.csbiginteger_to_string.argtypes = [
    ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
csbiginteger_lib.csbiginteger_to_string.restype = ctypes.c_bool
# csbiginteger_init_s(char* value, int base, byte* vr, int sz_vr);
csbiginteger_lib.csbiginteger_init_s.argtypes = [
    ctypes.c_char_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]
csbiginteger_lib.csbiginteger_init_s.restype = ctypes.c_int
# csbiginteger_add(byte* big1, int sz_big1, byte* big2, int sz_big2, byte* vr, int sz_vr) -> int
csbiginteger_lib.csbiginteger_add.argtypes = [
    ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]
csbiginteger_lib.csbiginteger_add.restype = ctypes.c_int
# csbiginteger_sub(byte* big1, int sz_big1, byte* big2, int sz_big2, byte* vr, int sz_vr) -> int
csbiginteger_lib.csbiginteger_sub.argtypes = [
    ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]
csbiginteger_lib.csbiginteger_sub.restype = ctypes.c_int
# csbiginteger_mul(byte* big1, int sz_big1, byte* big2, int sz_big2, byte* vr, int sz_vr) -> int
csbiginteger_lib.csbiginteger_mul.argtypes = [
    ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]
csbiginteger_lib.csbiginteger_mul.restype = ctypes.c_int
# csbiginteger_div(byte* big1, int sz_big1, byte* big2, int sz_big2, byte* vr, int sz_vr) -> int
csbiginteger_lib.csbiginteger_div.argtypes = [
    ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]
csbiginteger_lib.csbiginteger_div.restype = ctypes.c_int
# csbiginteger_mod(byte* big1, int sz_big1, byte* big2, int sz_big2, byte* vr, int sz_vr) -> int
csbiginteger_lib.csbiginteger_mod.argtypes = [
    ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]
csbiginteger_lib.csbiginteger_mod.restype = ctypes.c_int
# csbiginteger_shr(byte* big1, int sz_big1, byte* big2, int sz_big2, byte* vr, int sz_vr) -> int
csbiginteger_lib.csbiginteger_shr.argtypes = [
    ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]
csbiginteger_lib.csbiginteger_shr.restype = ctypes.c_int
# csbiginteger_shl(byte* big1, int sz_big1, byte* big2, int sz_big2, byte* vr, int sz_vr) -> int
csbiginteger_lib.csbiginteger_shl.argtypes = [
    ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]
csbiginteger_lib.csbiginteger_shl.restype = ctypes.c_int
# csbiginteger_eq(byte* big1, int sz_big1, byte* big2, int sz_big2) -> bool
csbiginteger_lib.csbiginteger_eq.argtypes = [
    ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]
csbiginteger_lib.csbiginteger_eq.restype = ctypes.c_bool
# csbiginteger_gt(byte* big1, int sz_big1, byte* big2, int sz_big2) -> bool
csbiginteger_lib.csbiginteger_gt.argtypes = [
    ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]
csbiginteger_lib.csbiginteger_gt.restype = ctypes.c_bool
# csbiginteger_lt(byte* big1, int sz_big1, byte* big2, int sz_big2) -> bool
csbiginteger_lib.csbiginteger_lt.argtypes = [
    ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]
csbiginteger_lib.csbiginteger_lt.restype = ctypes.c_bool


# ======================================================================
# BigInteger class stores a little-endian ctypes bytearray on self._data
# The total allocated size of self._data is self._datasize (bytes), and its used size is self._length (bytes).
# ======================================================================

@total_ordering
class BigInteger(object):
    def __init__(self, param=0, base: int = 10) -> T:
        """
        Create a BigInteger from the supplied input data
        Args:
            param: the input data to create an instance from. Accepted types: float, int, str, bytes/bytearray.
               bytes are parsed assuming little endian.
            base: only used when converting from `str` type
        """
        # 256 bytes, standard size (TODO: improve this with better logic, but now it's enough)
        self.std_size = 256
        if type(param) is float:
            param = int(param)
        if type(param) is int:
            param = str(param)  # convert to base-10 integer
            base = 10  # force base 10
        if type(param) is bytearray:
            param = bytes(param)  # bytearray to bytes
        if type(param) is bytes:
            self._length = len(param)
            self._data = (ctypes.c_uint8 * self._length).from_buffer(bytearray(param))
        if type(param) is str:
            # allocate a standard buffer size to use in the library
            self._data = (ctypes.c_uint8 * self.std_size)()

            strsize = len(param)
            strdata = (ctypes.c_char * strsize).from_buffer(bytearray(param, 'ascii'))

            sz = csbiginteger_lib.csbiginteger_init_s(strdata, base, self._data, self.std_size)
            if sz == 0:
                raise ValueError('Something wrong with BigInteger. Zero size.')
            self._length = sz

            # trim data to exact length
            alloc = (ctypes.c_uint8 * self._length)
            new_data = alloc.from_buffer(bytearray(self._data)[:self._length])
            self._data = new_data

        # more options here?

    def __int__(self) -> int:
        """
        Convert value to `int` type.

        Raises:
            OverflowError: if value does not fit in an `int` according to the C# rules

        Returns:
             int: value in signed int32 limit
        """
        if self.__gt__(2**31-1):
            raise OverflowError("overflow on signed int32")
        if self.__lt__(-2**31):
            raise OverflowError("underflow on signed int32")
        return int(str(self))

    def __float__(self) -> float:
        """
        Convert value to `long` type.

        Raises:
            OverflowError: if value does not fit in a `long` according to the C# rules

        Returns:
             long: value in signed int32 limit
        """
        if self.__gt__(2**63-1):
            raise OverflowError("overflow on signed int64 (long)")
        if self.__lt__(-2**63):
            raise OverflowError("underflow on signed int64 (long)")
        return float(self)

    def __hex__(self) -> str:
        return self.__to_str(self, base=16)

    @classmethod
    def from_bytes(cls: Type[T], data: bytes, byteorder: str = 'little', signed: bool = True) -> T:
        """

        Args:
            data: input data
            byteorder: the byte order used to represent the BigInteger. If byteorder is 'big',
               the most significant byte is at the beginning of the byte array. If
               byteorder is 'little', the most significant byte is at the end of the
               byte array. To request the native byte order of the host system, use
               `sys.byteorder' as the byte order value.
            signed: will throw an error if set to False as BigInteger is supposed to always be signed.
               This flag exists to give the same interface as the default int allowing to drop this class in
               as a replacement while notifying the user when operated incorrectly.

        Returns:
            BigInteger
        """
        if signed is False:
            raise ValueError("BigInteger can only be used in signed mode")

        if type(data) not in [bytearray, bytes]:
            raise ValueError("data must be bytes or bytearray")

        if byteorder == 'big':
            data = bytearray(data)
            data.reverse()
        return cls(data)

    def to_bytes(self, length: int, byteorder: str) -> bytearray:
        """
        Return an array of bytes representing an integer

        Args:
            length: Length of bytes object to use.
                An OverflowError is raised if the integer is not representable with the given number of bytes.
            byteorder: The byte order used to represent the integer.
                If byteorder is 'big', the most significant byte is at the beginning of the byte array. If
                byteorder is 'little', the most significant byte is at the end of the byte array. To request
                the native byte order of the host system, use `sys.byteorder' as the byte order value.

        Returns:
             bytearray: a byte array in the specified byteorder representing the BigInteger value
        """
        if length < self._length:
            raise OverflowError()

        if byteorder == 'big':
            data = bytearray(self._data)[:self._length]
            data.reverse()
            return data

        return bytearray(self._data)[:self._length]

    def __to_str(self, base: int = 16) -> str:
        # TODO: calculate precise size here (for base 10 and 2 for example). for 16 is std_size*2
        strsize = self.std_size*100
        strdata = (ctypes.c_char*strsize)()
        rbool = csbiginteger_lib.csbiginteger_to_string(
            self._data, self._length, base, strdata, strsize)
        if not rbool:
            raise ValueError('Something wrong with BigInteger to_str()')
        return strdata.value.decode()

    """
    Support build-ins
    """
    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return self.__to_str(base=10)

    def __len__(self) -> int:
        return self._length

    """
    Binary arithmetic operators
    """
    def __add__(self, other) -> T:
        if type(other) is int:
            other = self.__class__(other)

        _data = bytes(self.std_size)
        _data_sz = ctypes.c_int(self.std_size)

        len = csbiginteger_lib.csbiginteger_add(self._data, self._length, other._data, other._length, _data, _data_sz)

        if len == 0:
            raise ValueError('Something wrong with BigInteger add()')

        return self.__class__(_data[:len])

    def __sub__(self, other) -> T:
        if type(other) is int:
            other = self.__class__(other)

        _data = bytes(self.std_size)
        _data_sz = ctypes.c_int(self.std_size)

        len = csbiginteger_lib.csbiginteger_sub(self._data, self._length, other._data, other._length, _data, _data_sz)

        if len == 0:
            raise ValueError('Something wrong with BigInteger sub()')

        return self.__class__(_data[:len])

    def __mul__(self, other) -> T:
        if type(other) is int:
            other = self.__class__(other)

        _data = bytes(self.std_size)
        _data_sz = ctypes.c_int(self.std_size)

        len = csbiginteger_lib.csbiginteger_mul(self._data, self._length, other._data, other._length, _data, _data_sz)

        if len == 0:
            raise ValueError('Something wrong with BigInteger mul()')

        return self.__class__(_data[:len])

    def __floordiv__(self, other) -> T:
        """
            note that python usually follows 'pure floor' operation here, on a // b => floor(a/b)
            example: -5 // 2 => -3 (standard int on python)
            however, this library follows hardware-standard (from c/c++/java/fortran), of truncating positive or negative
            so, here: BigInteger(-5) // BigInteger(2) => -2 ("rounding" up, not down)
            floordiv is thus not a good name, since it's only floor for positive division, but ceil for negative, but that's what we have :)
        """

        if type(other) is int:
            other = self.__class__(other)

        _data = bytes(self.std_size)
        _data_sz = ctypes.c_int(self.std_size)

        len = csbiginteger_lib.csbiginteger_div(self._data, self._length, other._data, other._length, _data, _data_sz)

        if len == 0:
            raise ValueError('Something wrong with BigInteger div()')

        return self.__class__(_data[:len])

    def __truediv__(self, other) -> T:
        """
        truediv does not exist (using a // b)
        """
        return self.__floordiv__(other)

    def __mod__(self, other) -> T:
        if type(other) is int:
            other = self.__class__(other)

        _data = bytes(self.std_size)
        _data_sz = ctypes.c_int(self.std_size)

        len = csbiginteger_lib.csbiginteger_mod(self._data, self._length, other._data, other._length, _data, _data_sz)

        if len == 0:
            raise ValueError('Something wrong with BigInteger mod()')

        return self.__class__(_data[:len])

    def __rshift__(self, other) -> T:
        if type(other) is int:
            other = self.__class__(other)

        _data = bytes(self.std_size)
        _data_sz = ctypes.c_int(self.std_size)

        len = csbiginteger_lib.csbiginteger_shr(self._data, self._length, other._data, other._length, _data, _data_sz)
        if len == 0:
            raise ValueError('Something wrong with BigInteger shr()')

        return self.__class__(_data[:len])

    def __lshift__(self, other) -> T:
        if type(other) is int:
            other = BigInteger(other)

        _data = bytes(self.std_size)
        _data_sz = ctypes.c_int(self.std_size)

        len = csbiginteger_lib.csbiginteger_shl(self._data, self._length, other._data, other._length, _data, _data_sz)
        if len == 0:
            raise ValueError('Something wrong with BigInteger shl()')

        return self.__class__(_data[:len])

    """
    Rich comparison methods            
    """
    def __eq__(self, other) -> bool:
        if type(other) is int:
            other = self.__class__(other)
        ret = csbiginteger_lib.csbiginteger_eq(
            self._data, self._length, other._data, other._length)
        return ret

    def __gt__(self, other) -> bool:
        if type(other) is int:
            other = self.__class__(other)

        ret = csbiginteger_lib.csbiginteger_gt(self._data, self._length, other._data, other._length)
        return ret

    def __lt__(self, other) -> bool:
        if type(other) is int:
            other = self.__class__(other)

        ret = csbiginteger_lib.csbiginteger_lt(self._data, self._length, other._data, other._length)
        return ret

    """
    Unary arithmetic operators
    """
    def __abs__(self) -> T:
        if self < 0:
            return -self
        return self

    def __neg__(self) -> T:
        return self * -1
