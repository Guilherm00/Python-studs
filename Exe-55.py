#maior e menor peso 55
pesos=[]
for p in range(5):
  peso = int (input("Digite o seu peso: "))
  pesos.append(peso)
maior= max(pesos)
menor = min(pesos)
print("{} é o maior peso".format(maior))
print("{} é o menor peso".format(menor))