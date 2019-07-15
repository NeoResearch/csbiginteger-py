#!/usr/bin/python3

import ctypes
#from ctypes import * 

import os
import os.path
import re

csbiginteger_lib = ctypes.cdll.LoadLibrary('csbiginteger/csbiginteger.so')
#csbiginteger_lib = ctypes.cdll.LoadLibrary('./csbiginteger.so')
# init_empty
csbiginteger_lib.csbiginteger_init_empty.argtypes = [ctypes.c_void_p, ctypes.c_int]
csbiginteger_lib.csbiginteger_init_empty.restype  = ctypes.c_int
#to_int (32 bits)
csbiginteger_lib.csbiginteger_to_int.argtypes = [ctypes.c_void_p, ctypes.c_int]
csbiginteger_lib.csbiginteger_to_int.restype  = ctypes.c_int
#to_long (64 bits)
csbiginteger_lib.csbiginteger_to_long.argtypes = [ctypes.c_void_p, ctypes.c_int]
csbiginteger_lib.csbiginteger_to_long.restype  = ctypes.c_long
# csbiginteger_init_l (int64)
csbiginteger_lib.csbiginteger_init_l.argtypes = [ctypes.c_long, ctypes.c_void_p, ctypes.c_int]
csbiginteger_lib.csbiginteger_init_l.restype  = ctypes.c_int
# csbiginteger_to_string (byte* vb, int sz_vb, int base, char* sr, int sz_sr) -> bool
csbiginteger_lib.csbiginteger_to_string.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
csbiginteger_lib.csbiginteger_to_string.restype  = ctypes.c_bool
# csbiginteger_init_s(char* value, int base, byte* vr, int sz_vr);
csbiginteger_lib.csbiginteger_init_s.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]
csbiginteger_lib.csbiginteger_init_s.restype  = ctypes.c_int
#csbiginteger_add(byte* big1, int sz_big1, byte* big2, int sz_big2, byte* vr, int sz_vr) -> int 
csbiginteger_lib.csbiginteger_add.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]
csbiginteger_lib.csbiginteger_add.restype  = ctypes.c_int
#csbiginteger_sub(byte* big1, int sz_big1, byte* big2, int sz_big2, byte* vr, int sz_vr) -> int
csbiginteger_lib.csbiginteger_sub.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int]
csbiginteger_lib.csbiginteger_sub.restype  = ctypes.c_int

class BigInteger(object):
    # param may be: int, bytearray, string (parsed with base)
    def __init__(self, param = 0, base = 10):
        self.std_size = 256 # 256 bytes, standard size (TODO: improve this with better logic, but now it's enough)
        if type(param) is int:
            self._datasize = self.std_size
            self._data = (ctypes.c_uint8*self._datasize)()
            sz = 0
            if param == 0:
                sz = csbiginteger_lib.csbiginteger_init_empty(self._data, self._datasize)
            else:
                sz = csbiginteger_lib.csbiginteger_init_l(param, self._data, self._datasize)
            if sz == 0:
                raise ValueError('Something wrong with BigInteger. Zero size.')
            self._length = sz
        if type(param) is bytearray:
            param = bytes(param) # bytearray to bytes
        if type(param) is bytes:
            self._length = len(param)
            self._datasize = self._length  # size is not standard, is less. exactly what is needed
            self._data = (ctypes.c_uint8*self._datasize).from_buffer(bytearray(param))
        if type(param) is str:
            self._datasize = self.std_size
            self._data = (ctypes.c_uint8*self._datasize)()
            strsize = len(param)
            strdata = (ctypes.c_char*strsize).from_buffer(bytearray(param, 'ascii'))
            sz = csbiginteger_lib.csbiginteger_init_s(strdata, base, self._data, self._datasize)
            if sz == 0:
                raise ValueError('Something wrong with BigInteger. Zero size.')
            self._length = sz
        
        # more options here?

    def length(self):
        return self._length

    def to_int(self):
        return csbiginteger_lib.csbiginteger_to_int(self._data, self._length)

    def to_long(self):
        return csbiginteger_lib.csbiginteger_to_long(self._data, self._length)

    def to_str(self, base=16):
        strsize = self.std_size*2
        strdata = (ctypes.c_char*strsize)()
        rbool = csbiginteger_lib.csbiginteger_to_string(self._data, self._length, base, strdata, strsize)
        if not rbool:
            raise ValueError('Something wrong with BigInteger to_str()')
        return strdata.value.decode()

    def add(self, other):
        big3 = BigInteger() # create new array
        ret = csbiginteger_lib.csbiginteger_add(self._data, self._length, other._data, other._length, big3._data, big3._datasize)
        if ret == 0:
            raise ValueError('Something wrong with BigInteger add()')
        return big3

    def sub(self, other):
        big3 = BigInteger() # create new array
        ret = csbiginteger_lib.csbiginteger_sub(self._data, self._length, other._data, other._length, big3._data, big3._datasize)
        if ret == 0:
            raise ValueError('Something wrong with BigInteger sub()')
        return big3
