#all:
#	g++ --shared csBigIntegerpp/src/csBigIntegerLib.cpp csBigIntegerpp/src/BigInteger.cpp -lgmp -lgmpxx -o csbiginteger/csbiginteger.so -fPIC

# test python
run:
	./test.py
#	export LD_LIBRARY_PATH=. && ./test.py

vendor:
	@echo "trying to install GNU lgmp library (debian-based systems)"
	sudo apt-get install libgmp-dev
	# submodule inside submodule... don't know how to handle it here. better directly go to 'csBigInteger.cpp' project
	#@echo "trying to configure libgtest on csBigIntegerpp/tests/"
	#(cd csBigIntegerpp/tests/libgtest && mkdir -p build && cd build && cmake .. && make)
	@echo "compiling csBigInteger.cpp portable project"
	(cd csBigIntegerpp && make && cp build/*.so ../csbiginteger/)


clean:
	#rm build/*.so 
	rm csbiginteger/*.pyc
