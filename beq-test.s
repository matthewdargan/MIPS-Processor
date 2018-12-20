addi $s0, $zero, 5
addi $s1, $zero, 5
addi $t1, $zero, 8
beq $s0, $s1, here
add $t1, $t1, $t2
here: or $s2, $s0, $t1
