#!/usr/bin/python

import ctypes
#from ctypes import * 

import os
import os.path
import re

csbiginteger_lib = ctypes.cdll.LoadLibrary('csBigInteger/csbiginteger.so')
# init_empty
csbiginteger_lib.csbiginteger_init_empty.argtypes = [ctypes.c_void_p, ctypes.c_int]
csbiginteger_lib.csbiginteger_init_empty.restype  = ctypes.c_int
#to_int (32 bits)
csbiginteger_lib.csbiginteger_to_int.argtypes = [ctypes.c_void_p, ctypes.c_int]
csbiginteger_lib.csbiginteger_to_int.restype  = ctypes.c_int


class BigInteger:
    def __init__(self):
        self.std_size = 256 # 256 bytes, standard size (TODO: improve this with better logic, but now it's enough)
        self._datasize = self.std_size
        self._data = (ctypes.c_uint8*self._datasize)()
        sz = self.initEmpty(self._data, self._datasize)
        if sz == 0:
            raise ValueError('Something wrong with BigInteger. Zero size.')
        self._length = sz

    # auxiliar method, make it private (and static)
    def initEmpty(self, data, datasize):
        sz = csbiginteger_lib.csbiginteger_init_empty(data, datasize)
        return sz

    def length(self):
        return self._length

    def toInt(self):
        return csbiginteger_lib.csbiginteger_to_int(self._data, self._datasize)
