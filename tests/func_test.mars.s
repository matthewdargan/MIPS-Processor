ori $sp,$zero,0
addi $t0, $zero, 12
add $a0, $t0, $zero
jal mul3
add $t0, $v0, $zero 
j exit

mul3:
add $t1, $a0, $a0
add $t1, $t1, $a0
add $v0, $zero, $t1
jr $ra

exit:
ori $s0, $t0, 0
ori $s1, $ra, 0  # check latest return address
