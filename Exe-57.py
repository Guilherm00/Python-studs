#Identificador de sexos 57
while True:
  resp = input("Digite o sexo [F/M]: ").upper()
  if resp in ['M','F']:
    print ("Sexo {} Selecionado".format(resp))
    reiniciar = input("Deseja reiniciar o programa?[S/N]: ").upper()
    if reiniciar != 'S':
      print("Programa encerrado. Adeus!")
      break
    else:
      continue
  else:
    print("Opção inválida. Tente novamente.")