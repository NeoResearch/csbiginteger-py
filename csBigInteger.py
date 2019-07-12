#!/usr/bin/python

import ctypes
from ctypes import *   #import Structure

import os
import os.path
import re

class BigInteger:
    def __init__(self):
        self.lib = ctypes.cdll.LoadLibrary('./build/csbiginteger.so')
        self.lib.csbiginteger_init_empty.argtypes = [ctypes.c_void_p, ctypes.c_int]
        self.lib.csbiginteger_init_empty.restype  = ctypes.c_int

    def initEmpty(self, data, datasize):
        sz = self.lib.csbiginteger_init_empty(data, datasize)
        return sz
