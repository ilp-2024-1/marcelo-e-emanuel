#Q01 WHILE
valor = 1
while valor <= 100:
  print(valor)
  valor += 1
print("finalizado, o valor chegou a 100.")


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


#Q03 WHILE

senha= "1234"
chute = input("Digite uma senha (dica: contém 4 digitos): ")
while chute != senha:
  chute = input("Senha incorreta. Tente denovo: ")
  if chute == senha:
    print("Senha correta.")


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


#Q05 WHILE

valor = int(input("Digite um número inteiro positivo: "))
if valor <= 0:
  print(valor, "não é um número inteiro positivo.")
else:
  n = 1
  fatorial = 1
  while n <= valor:    
    fatorial = fatorial * n    
    n = n + 1
  print("O fatorial de", valor, "é", fatorial)


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


#Q07 WHILE
while True:
    numero = int(input("Digite um número entre 1 e 10000:"))
    
    if numero <= 0 or numero >= 10001:
        print("Número não esta entre os numeros informados, progama encerrado.")
        break

    if numero == 1:
        print("O numéro 1 não é primo, progama encerrado.")
    else:
        divisor = 2
        primo = True

        while divisor < numero:
            if numero % divisor == 0:
                primo = False
                break
            divisor += 1

        if primo:
            print(f"O número {numero} é primo, progama encerrado.")
        else:
            print(f"O número {numero} não é primo, progama encerrado.")

    break
        

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


#Q09 WHILE

numero = int(input("Digite um número inteiro positivo n: "))
soma = 0.0
termo = 1
while termo <= numero:
    soma += 1 / termo
    termo += 1
print(f"A soma da série harmônica até o {numero} termo é: {soma}, progama encerrado.")







