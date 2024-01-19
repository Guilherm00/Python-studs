#programa de conversao
print("Este é um program de conversão de numeros decimais ^^")
num = int (input("digite o numero que deseja converter: "))
print ('''Escolha uma base de conversão:
[1] converter para BINÁRIO
[2] converter para HEXADECIMAL
[3] converter para OCTAL ''')

opcao = int (input("Escolha uma opção: "))
if opcao == 1:
 print("{} Convertido para Binário é {}".format(num, bin(num)[2:]))
elif opcao == 2:
  print("{} Convertido para Hexadecimal é {}".format(num, hex(num)[2:]))
elif opcao == 3:
  print("{} Convertido para Octal é {}".format(num, oct(num)[2:]))
else :
  print ("numero INVALIDO, escolha uma opção válida")
