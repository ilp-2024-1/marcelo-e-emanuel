# questao 01 - Escreva um programa que exiba os valores dos números de 1 até 100. Ao término o programa deverá exibir uma mensagem de encerramento informando que o programa terminou.

valor = 0
while valor != 100:
  valor = valor + 1

  print(valor)

# questao 02 - Escreva um programa que solicita ao usuário valores numéricos e realiza a soma desses valores. Quando o usuário digitar o valor 0 o programa deverá exibir o valor do 
# somatório e encerrar o programa com uma mensagem de término do programa. O usuário deverá ser informado no início do programa o que o programa faz e qual a condição para 
# encerramento do programa.

print("Este programa soma os valores numéricos inseridos pelo usuário.")
print("Para encerrar, digite 0.")

soma = 0
valor = None

while valor != 0:
  valor = float(input("Digite um valor numérico (ou 0 para encerrar): "))
  if valor != 0:
    soma += valor

print ("O valor da soma é: {soma}.")
print ("O programa terminou.")

# questao 03 - Crie um programa que solicita ao usuário uma senha e em seguida compare esse valor com uma senha armazenada em uma variável. Enquanto o usuário não acertar o valor 
# da senha o programa deverá solicitar a senha ao usuário. Quando o usuário acerta a senha, o programa deverá encerrar exibindo uma mensagem encerramento e informar que o usuário 
# acertou a senha.

# questao 04 - Escreva um programa que gere um número aleatório entre 1 e 100 e peça ao usuário para adivinhar qual é o número. O programa deve continuar pedindo palpites até que 
# o usuário acerte o número. Ao final, o programa deve informar quantos palpites foram necessários e informar que o programa encerrou.

