#soma de numeros ímpares 48
n = 0
for p in range(1,500):
  if p % 3 == 0 :
    n = n+p
print("A soma dos números ímpares que são multiplo de 3 é: {}".format(n))