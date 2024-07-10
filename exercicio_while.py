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

# questao 04 - Escreva um programa que gere um número aleatório entre 1 e 100 e peça ao usuário para adivinhar qual é o número. O programa deve continuar pedindo palpites até que 
# o usuário acerte o número. Ao final, o programa deve informar quantos palpites foram necessários e informar que o programa encerrou.

import random
numero = random.randint(1, 100)
palpites = 0

while True:
    palpites = int(input("Adivinhe o número entre 1 e 100: "))
    palpites += 1
    if palpites == numero:
        print("Parabéns! Você acertou em {palpites} palpites.")
        break
    elif palpites < numero:
        print("Maior.")
    else:
        print("Menor.")

print("Programa encerrado.")

# questao 06 - Escreva um programa que peça ao usuário para digitar um número “n” inteiro positivo e, em seguida, imprima os “n” primeiros termos da sequência de Fibonacci. A
# sequência de Fibonacci é dada pela somatório de dois números que resulta no seu sucessor. Ex: 0, 1, 1, 2, 3, 5, 8... Esses são os 7 primeiros números da sequência.
# Exiba os números na tela e informa o término do programa ao final.

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Digite um número inteiro positivo: "))

if n > 0:
    print("Os {n} primeiros termos da sequência de Fibonacci são:")
    fibonacci(n)
else:
    print("Por favor, digite um número inteiro positivo.")

print("\nPrograma encerrado.")

# questao 8 -  Escreva um programa que peça ao usuário para digitar um número inteiro e, em seguida, calcule a soma dos dígitos desse número usando um loop while. Ao término, 
# informe que o programa foi encerrado. Ex: entrada: 19.623 à saída: 21; entrada: 456 à saída: 15;

def soma_digitos(numero):
    soma = 0
    while numero > 0:
        digito = numero % 10
        soma += digito
        numero //= 10
    return soma

numero = int(input("Digite um número inteiro: "))
resultado = soma_digitos(abs(numero))

print("A soma dos dígitos de {numero} é {resultado}.")
print("Programa encerrado.")