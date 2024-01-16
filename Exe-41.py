#programa de classificação 41
from datetime import datetime
data_nasc = int (input("Ano de nascimento:"))
ano_atual = datetime.now().year
idade = ano_atual - data_nasc

if idade <=9 :
  print("Você tem {} ano(s) de idade sua categoria é a MIRIM ! ".format(idade))
elif idade  <=14:
  print('Você tem {} ano(s) de idade sua categoria é a INFANTIL !'.format(idade))
elif idade  <=19:
  print('Você tem {} ano(s) de idade sua categoria é a JÚNIOR !'.format(idade))
elif idade  <=25:
  print('Você tem {} ano(s) de idade sua categoria é a SÊNIOR !'.format(idade))
else :
  print('Você tem {} ano(s) de idade sua categoria é a MASTER !'.format(idade))
    
