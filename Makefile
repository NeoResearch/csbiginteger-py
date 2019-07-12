all:
	g++ --shared csBigIntegerpp/src/csBigIntegerLib.cpp csBigIntegerpp/src/BigInteger.cpp -lgmp -lgmpxx -o csbiginteger/csbiginteger.so -fPIC

# test python
run:
	./test.py
#	export LD_LIBRARY_PATH=. && ./test.py

clean:
	#rm build/*.so 
	rm csBigInteger/*.pyc
