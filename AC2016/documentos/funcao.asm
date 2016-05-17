# def soma (a, b)
#    return a + b
# soma(10, 20)

.text
.globl main
main:
	sub $sp, $sp, 12 # Aloca 3 espacos (cada um de 4 bits) na pilha
	addi $s0, $zero, 10 # Define 10 a s0
	addi $s1, $zero, 20 # Define 20 a s1
	sw $s0, 0($sp) # Coloca na fila o primeiro parametro
	sw $s1, 4($sp) # Coloca na fila o segundo parametro
	jal soma # Chama o Label da funcao soma atraves do jal
	lw $s2, 0($sp) # Obtem o resultado da funcao (o retorno)
	add $sp, $sp, 12 # Desaloca 3 espacaos na pilha
	syscall # Finaliza o programa
	
soma:
	sw $ra, 8($sp) # Grava o endereço de retorno na pilha
	lw $t0, 0($sp) # Carrega primeiro parametro
	lw $t1, 4($sp) # Carrega segundo parametro
	add $t0, $t0, $t1 # Realiza a soma de a + b
	sw $t0, 0($sp) # Grava o resultado da soma na pilha
	lw $ra, 8($sp) # Carrega o endereço de retorno
	jr $ra # Retorna ao codigo principal
