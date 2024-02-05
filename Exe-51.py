#PROGRESSAO ARITIMETICA 51
pt = int (input("Qual o primeiro termo? "))
r = int (input("Qual a razão?"))
for i in range(0,10+1):
  progressao = pt + (i*r)
  print(progressao,end=", ")
print("")
print("O primeiro termo é : {}".format(pt))
print("A razão é : {}".format(r))
