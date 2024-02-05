#soma de pares 50
soma = 0
for n in range(0,6):
  n1 = int (input("digite um numero: "))
  if n1 % 2 ==0 :
   soma += n1
print ("A soma dos números pares é:{}".format(soma))