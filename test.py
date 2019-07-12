#!/usr/bin/python
# basic example from SimplePyCuda library
# MIT License - Igor Machado Coelho (2017)

import ctypes

from csBigInteger import BigInteger

import numpy
'''
def simpleLoadTest(cuda):
	lib = ctypes.cdll.LoadLibrary('./__simplepycuda_kernel_doublify.so')
	lib.kernel_loader.argtypes = [ctypes.c_void_p, grid, block, ctypes.c_ulong, ctypes.c_ulong]
	a = numpy.random.randn(4,4)
	a_gpu = cuda.mem_alloc(a.nbytes)
	lib.kernel_loader(a_gpu, grid(1,1), block(4,4,1), 0, 0)
	print "Kernel OK"
	# finish

def classicExample(cuda):
	a = numpy.random.randn(4,4)
	a = a.astype(numpy.float32)
	print a
	a_gpu = cuda.mem_alloc(a.nbytes)
	cuda.memcpy_htod(a_gpu, a)
	mod = SimpleSourceModule(""" 
          #include<stdio.h>
          __global__ void doublify ( float* a )
	  {
	    int idx = threadIdx.x + threadIdx.y*4;
	    a[idx] *= 2;
            printf("oi=%d\\n",idx);
	  }
	""","nvcc", ["--ptxas-options=-v","--compiler-options -O3","--compiler-options -Wall"])
	func = mod.get_function("doublify")
	# TODO: this next line will be made automatically in get_function method... just need a few more time :)
	func.argtypes = [ctypes.c_void_p, grid, block, ctypes.c_ulong, ctypes.c_ulong]
	func(a_gpu, grid(1,1), block(4,4,1), 0, 0)
	cuda.memcpy_dtoh(a, a_gpu)
	cuda.deviceSynchronize()
	print a
	cuda.free(a_gpu) # this is not necessary in PyCUDA
	print "Finished"
'''

def main():
    big = BigInteger()
    data = (ctypes.c_uint8*5)()
    sz = big.initEmpty(data, 5)
    print('size = ', sz)
    return 0

if __name__ == '__main__':
    main()


