# INDICE DE IMC
alt = float (input("Informe sua altura:"))
peso = float (input("Informe seu peso:"))

imc =  peso / (alt**2)
print ("seu IMC é: {:.1f}".format(imc))

if imc <= 18.5 :
  print ("ABAIXO DO PESO NORMAL.")
elif  18.5 <= imc < 24.9 :
  print ("PESO NORMAL.")
elif  24.9 <= imc < 29.9:
  print ("SOBREPESO")
elif 29.9 <= imc < 34.9 :
  print ("OBESIDADE GRAU I")
elif 34.9 <= imc < 39.9 :
  print ("OBESIDADE GRAU II. CUIDADO")
elif imc >= 40:
  print ("OBESIDADE GRAU III. CUIDADO")
