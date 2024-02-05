#identificador de palindromo 53
s = str (input("Escreva sua frase: "))
inverso = ""
s = s.replace(" ", "").lower()
for letra in s:
  inverso = letra + inverso
if s == inverso:
  print("{} é um palíndromo!".format(s))
else:
    print("{} não é um palíndromo.".format(s))
