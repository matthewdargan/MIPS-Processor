# Run MIPS single-cycle tests
p2sc:
	cp alu.circ regfile.circ mem.circ cpu.circ tests
	cd tests && python ./test.py p2sc | tee ../TEST_LOG

# Run MIPS 2-stage pipelined tests
p2:
	cp alu.circ regfile.circ mem.circ cpu.circ tests
	cd tests && python ./test.py p2 | tee ../TEST_LOG

# Run ALU + Regfile tests
p1:
	cp alu.circ regfile.circ tests
	cd tests && python ./test.py p1 | tee ../TEST_LOG
