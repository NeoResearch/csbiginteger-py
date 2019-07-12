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


class BigInteger(object):
    # how to pass null parameters, or multiple?
    def __init__(self, param = 0):
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
        if type(param) is bytes:
            self._length = len(param)
            self._datasize = self._length
            self._data = (ctypes.c_uint8*self._datasize).from_buffer(bytearray(param))
        # 

    def length(self):
        return self._length

    def toInt(self):
        return csbiginteger_lib.csbiginteger_to_int(self._data, self._length)

    def toLong(self):
        return csbiginteger_lib.csbiginteger_to_long(self._data, self._length)

    def toString(self, base=16):
        strsize = self.std_size*2
        strdata = (ctypes.c_char*strsize)()
        rbool = csbiginteger_lib.csbiginteger_to_string(self._data, self._length, base, strdata, strsize)
        if not rbool:
            raise ValueError('Something wrong with BigInteger ToString()')
        return strdata.value.decode()
