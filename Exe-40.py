#program de media escolar 40
nota1 = float (input("insira a primeira nota:"))
nota2 = float (input("insira a segunda nota:"))
media = (nota1 + nota2) / 2

print('sua media é:')
print(media)
if media < 5 :
  print("Parabés você foi incompetente REPROVADO")
  print("sua média é :{}".format(media))
elif media > 7 :
 print("Parabéns você fes o minimo e tirou a media APROVADO")
 print("sua média é :{}".format(media))
elif media > 5  < 6.9 :
  print("Olha você foi quase mediano mas vc TA DE RECUPERAÇÃO xD")
  print("sua média é :{}".format(media))
elif media >= 10 :
  print('CARACA você é brabo aprovadissivo!!')
  print("sua média é :{}".format(media))