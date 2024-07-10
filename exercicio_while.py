#Q01 WHILE
valor = 1
while valor <= 100:
  print(valor)
  valor += 1
print("finalizado, o valor chegou a 100.")

#Q03 WHILE

senha= "1234"
chute = input("Digite uma senha (dica: contém 4 digitos): ")
while chute != senha:
  chute = input("Senha incorreta. Tente denovo: ")
  if chute == senha:
    print("Senha correta.")

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
        
#Q09 WHILE

numero = int(input("Digite um número inteiro positivo n: "))
soma = 0.0
termo = 1
while termo <= numero:
    soma += 1 / termo
    termo += 1
print(f"A soma da série harmônica até o {numero} termo é: {soma}, progama encerrado.")