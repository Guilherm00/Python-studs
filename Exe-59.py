#menu 59

nun1 = int(input("Informe o primeiro número: "))
nun2 = int(input("Informe o segundo número: "))
while True :
  print('''Oq você deseja fazer com esses numeros ?
[1] Soma
[2] Multiplicação
[3] Maior
[4] Novos números
[5] Sair do programa''')
  resp = int(input("Escolha uma opção: "))
  if resp == 1:
    soma = nun1 + nun2
    print ("A soma de {} + {} é igual a {}".format(nun1,nun2,soma))
  elif resp ==2 :
    multi = nun1*nun2
    print ("A Multiplicação de {} x {} é igual a {}".format(nun1,nun2,multi))
  elif resp == 3:
    maior = max(nun1,nun2)
    print("O maior número entre {} e {} é {}".format(nun1,nun2,maior))
  elif resp == 4 :
    nun1 = int(input("Informe o primeiro número: "))
    nun2 = int(input("Informe o segundo número: "))
  elif resp == 5:
    print("Volte sempre ^_^")
    break
  else:
    print("Opção invalida escolha uma opção de 1 a 5!!")
  retorno = input("Deseja escolher outra opção?[S/N]: ").upper()
  if retorno != ("S"):
    print("Volte sempre ^_^")
    break