#programa dos triangulos
r1 = float (input('Insira o primeiro segmento: '))
r2 = float (input('Insira o segundo segmento: '))
r3 = float (input('Insira o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  print (" Os segmentos PODEM formar um triângulo: ",end="")
  if r1 == r2 == r3 :
    print("Equilatero !")
  elif r1 != r2 != r3 != r1 :
    print("Escaleno !")
  else:
    print("Isósceles !")
else:
  print("os segmentos NÃO PODEM formar um triângulo")