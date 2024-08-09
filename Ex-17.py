import math
print("-="*5+ "HIPOTENUSAMENTE FALANDO" +"-="*5)
co = float(input("Qual o valor do cateto oposto?: "))
ca = float(input("Qual o valor do cateto adjacente?: "))
hp = math.hypot(co,ca)
print("O valor da Hipotenusa é {} ".format(hp))
print("-="*22)