all:
	g++ --shared csBigIntegerpp/src/csBigIntegerLib.cpp csBigIntegerpp/src/BigInteger.cpp -lgmp -lgmpxx -o build/csbiginteger.so -fPIC

# test python
run:
	export LD_LIBRARY_PATH=. && ./test.py

clean:
	rm *.so 