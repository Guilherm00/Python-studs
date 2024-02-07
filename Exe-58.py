#game da adivinhação 58
win = 0
lose = 0
from random import randint
while True:
  computador = randint (0,5)
  print("-=-"*20)
  print("Eu pensei em um numero de 1 a 5 você consegue advinhar?")
  print("-=-"*20)
  jogador = int (input("Digite seu palpite: "))
  if jogador == computador :
    print("PARABÉNS VOCÊ ACERTO !!")
    win = win + 1
    resp = input("Deseja jogar novamente ?[S/N]")
    if resp == ('S','s'):
      continue
    else:
      break
  else:
    print("Que pena você não acertou tente novamente")
    lose = lose + 1
print("PONTUAÇÃO FINAL")
print(" Jogador você precisou de {} tentativas para fazer {} pontos. ".format(lose,win))