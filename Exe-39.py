#programa de alistamento 39
from datetime import datetime
ano_nasc = int (input("Ano de nascimento:"))
ano_atual = datetime.now().year
idade = ano_atual - ano_nasc
if idade < 18 :
  tempo_falt = 18 - idade
  print("Voce ainda não pode se alistar ainda faltam {} anos !! ".format(tempo_falt)) 
elif idade == 18:
  print("Já esta na hora de se alistar, porfavor faça sua inscrição pelo: https://alistamento.eb.mil.br/ ")
  print("caso o prazo de inscrição vença você estará sujeito a uma multa !!")
elif idade > 100 :
  print ("essa não é uma idade valida porfavor refazer o teste")
else :
  tempo_atraso = 18 + idade 
  print("xiii você ta atrasado pro seu alistamento em {} anos!!".format(tempo_atraso)) 
  

  
