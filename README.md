# MIPS-Processor
## Overview
An implementation of a MIPS processor using [Logisim](http://www.cburch.com/logisim/) to build the circuitry and Python to test the processor itself.

![Screenshot](imgs/cpu1.png)
![Screenshot](imgs/cpu2.png)
![Screenshot](imgs/cpu3.png)

The project implements the following parts:
1. Regfile - for the necessary read/write ports and registers needed to store values
2. Memory - for storing values in long term memory when a programmer runs out of registers to use or needs to use a stack
2. ALU - for performing arithmetic instructions for the processor
3. Processor - for controlling the logic for instructions to compute correctly and update registers/memory when needed

## Supported Instructions
- sll
- srl
- sra
- add
- addu
- addiu
- addi
- jal
- jr
- j
- slt
- sltu
- sltiu
- slti
- and
- or
- andi
- ori
- lui
- lw
- sw
- beq
- bne
- clz