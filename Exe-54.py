#contador de maior idade 54
from datetime import datetime
contador = 0  
for idade in range(0,7):
  Data = int (input("digite o ano de nascimento: "))
  ano_atual = datetime.now().year
  idade = ano_atual - Data
  if idade < 21 :
    contador = contador + 1 
print("{} pessoas ainda não atingiram a maior idade".format(contador))