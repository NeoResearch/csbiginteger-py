#!/usr/bin/python3

import ctypes
#from ctypes import *

import os
import os.path
import re

csbiginteger_lib = ctypes.cdll.LoadLibrary('csbiginteger/csbiginteger.so')
#csbiginteger_lib = ctypes.cdll.LoadLibrary('./csbiginteger.so')
# init_empty
csbiginteger_lib.csbiginteger_init_empty.argtypes = [
    ctypes.c_void_p, ctypes.c_int]
csbiginteger_lib.csbiginteger_init_empty.restype = ctypes.c_int
# to_int (32 bits)
csbiginteger_lib.csbiginteger_to_int.argtypes = [ctypes.c_void_p, ctypes.c_int]
csbiginteger_lib.csbiginteger_to_int.restype = ctypes.c_int
# to_long (64 bits)
csbiginteger_lib.csbiginteger_to_long.argtypes = [
    ctypes.c_void_p, ctypes.c_int]
csbiginteger_lib.csbiginteger_to_long.restype = ctypes.c_long
# csbiginteger_init_l (int64)
csbiginteger_lib.csbiginteger_init_l.argtypes = [
    ctypes.c_long, ctypes.c_void_p, ctypes.c_int]
csbiginteger_lib.csbiginteger_init_l.restype = ctypes.c_int
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


class BigInteger(object):
    # param may be: int, bytearray, bytes, string (parsed with base)
    # bytes and bytearray should be received in little-endian format (same as to_bytearray() returns)
    def __init__(self, param=0, base=10):
        # 256 bytes, standard size (TODO: improve this with better logic, but now it's enough)
        self.std_size = 256
        if type(param) is int:
            param = str(param)  # convert to base-10 integer
            base = 10  # force base 10
        if type(param) is bytearray:
            param = bytes(param)  # bytearray to bytes
        if type(param) is bytes:
            self._length = len(param)
            # size is not standard, is less. exactly what is needed
            self._datasize = self._length
            self._data = (ctypes.c_uint8 *
                          self._datasize).from_buffer(bytearray(param))
        if type(param) is str:
            self._datasize = self.std_size
            self._data = (ctypes.c_uint8*self._datasize)()
            strsize = len(param)
            strdata = (ctypes.c_char *
                       strsize).from_buffer(bytearray(param, 'ascii'))
            sz = csbiginteger_lib.csbiginteger_init_s(
                strdata, base, self._data, self._datasize)
            if sz == 0:
                raise ValueError('Something wrong with BigInteger. Zero size.')
            self._length = sz

        # more options here?

    def length(self):
        return self._length

    # returns value in signed int32 limit (or exception)
    def to_int(self):
        return csbiginteger_lib.csbiginteger_to_int(self._data, self._length)

    def to_long(self):
        return csbiginteger_lib.csbiginteger_to_long(self._data, self._length)

    # bytearray is returned in little-endian format
    def to_bytearray(self):
        return bytearray(self._data)[:self._length]

    def to_str(self, base=16):
        # TODO: calculate precise size here (for base 10 and 2 for example). for 16 is std_size*2
        strsize = self.std_size*100
        strdata = (ctypes.c_char*strsize)()
        rbool = csbiginteger_lib.csbiginteger_to_string(
            self._data, self._length, base, strdata, strsize)
        if not rbool:
            raise ValueError('Something wrong with BigInteger to_str()')
        return strdata.value.decode()

    def add(self, other):
        if type(other) is int:
            other = BigInteger(other)
        big3 = BigInteger()  # create new array
        ret = csbiginteger_lib.csbiginteger_add(
            self._data, self._length, other._data, other._length, big3._data, big3._datasize)
        if ret == 0:
            raise ValueError('Something wrong with BigInteger add()')
        return big3

    def sub(self, other):
        if type(other) is int:
            other = BigInteger(other)
        big3 = BigInteger()  # create new array
        ret = csbiginteger_lib.csbiginteger_sub(
            self._data, self._length, other._data, other._length, big3._data, big3._datasize)
        if ret == 0:
            raise ValueError('Something wrong with BigInteger sub()')
        return big3

    def mul(self, other):
        if type(other) is int:
            other = BigInteger(other)
        big3 = BigInteger()  # create new array
        ret = csbiginteger_lib.csbiginteger_mul(
            self._data, self._length, other._data, other._length, big3._data, big3._datasize)
        if ret == 0:
            raise ValueError('Something wrong with BigInteger mul()')
        return big3

    def div(self, other):
        if type(other) is int:
            other = BigInteger(other)
        big3 = BigInteger()  # create new array
        ret = csbiginteger_lib.csbiginteger_div(
            self._data, self._length, other._data, other._length, big3._data, big3._datasize)
        if ret == 0:
            raise ValueError('Something wrong with BigInteger div()')
        return big3

    def mod(self, other):
        if type(other) is int:
            other = BigInteger(other)
        big3 = BigInteger()  # create new array
        ret = csbiginteger_lib.csbiginteger_mod(
            self._data, self._length, other._data, other._length, big3._data, big3._datasize)
        if ret == 0:
            raise ValueError('Something wrong with BigInteger mod()')
        return big3

    def shl(self, other):
        if type(other) is int:
            other = BigInteger(other)
        big3 = BigInteger()  # create new array
        ret = csbiginteger_lib.csbiginteger_shl(
            self._data, self._length, other._data, other._length, big3._data, big3._datasize)
        if ret == 0:
            raise ValueError('Something wrong with BigInteger shl()')
        return big3

    def shr(self, other):
        if type(other) is int:
            other = BigInteger(other)
        big3 = BigInteger()  # create new array
        ret = csbiginteger_lib.csbiginteger_shr(
            self._data, self._length, other._data, other._length, big3._data, big3._datasize)
        if ret == 0:
            raise ValueError('Something wrong with BigInteger shr()')
        return big3

    def eq(self, other):
        if type(other) is int:
            other = BigInteger(other)
        ret = csbiginteger_lib.csbiginteger_eq(
            self._data, self._length, other._data, other._length)
        return ret  # bool

    def lt(self, other):
        if type(other) is int:
            other = BigInteger(other)
        ret = csbiginteger_lib.csbiginteger_lt(
            self._data, self._length, other._data, other._length)
        return ret  # bool

    def gt(self, other):
        if type(other) is int:
            other = BigInteger(other)
        ret = csbiginteger_lib.csbiginteger_gt(
            self._data, self._length, other._data, other._length)
        return ret  # bool

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.to_str(10)

    # ---------
    # operators
    # ---------
    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.sub(other)

    def __mul__(self, other):
        return self.mul(other)

    def __floordiv__(self, other):
        return self.div(other)

    # truediv does not exist (using floordiv)
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

    def __gt__(self, other):
        return self.gt(other)

    def __lt__(self, other):
        return self.lt(other)
