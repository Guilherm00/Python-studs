#numeros primos 52
n = int(input("Digite um número inteiro: "))
if  n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)):
  print("O numero {} é primo!".format(n))
else:
  print("O número {} não é primo!".format(n))