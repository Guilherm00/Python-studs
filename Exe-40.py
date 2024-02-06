#program de media escolar 40
nota1 = float (input("insira a primeira nota:"))
nota2 = float (input("insira a segunda nota:"))
media = nota1 + nota2 / 2

print('sua media é:{:.1f}'.format(media))
if media < 5 :
  print("REPROVADO")
elif media > 7 :
 print("Tirou a media APROVADO")
elif media > 5  < 7 :
  print("Olha você foi quase mediano mas vc TA DE RECUPERAÇÃO xD")
elif media >= 10 :
  print('CARACA você é foi aprovadissivo!!')