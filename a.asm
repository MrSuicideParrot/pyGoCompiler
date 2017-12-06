main:
	li $t1, 1
	li $t2, 1
	add $t0, $t1, $t2
	li $v0, 1
	add $a0, $t0, $zero
	syscall
	li $v0, 11
	add $a0, 32, $zero
	syscall
	li $t1, 3
	li $t3, 3
	add $t2, $t1, $t3
	li $v0, 1
	add $a0, $t2, $zero
	syscall
	li $v0, 11
	add $a0, 32, $zero
	syscall
	li $v0, 1
	add $a0, 4, $zero
	syscall
