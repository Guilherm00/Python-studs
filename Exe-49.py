#tabuada 49
num = int (input("Qual tabuada você deseja:"))
for n in range(1,11):
  result = num * n
  print("{}x{}= {}".format(num,n,result) )