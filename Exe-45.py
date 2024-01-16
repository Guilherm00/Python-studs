#pedra, papel e tesoura
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print ('''ESCOLHA SUA JOGADA
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
player = int (input("Qual sua jogada? "))
print ("*"*20)
print ("O computador escolheu {}".format(itens[computador]))
print ("O jogador escolheu {}".format(itens[player]))
print ("*"*20)

if computador == 0 :#PEDRA
  if player == 0 :
    print ("EMPATE")
  elif player == 1 :
    print("Jogador Ganhou")
  elif player ==2 :
    print ("Computador Ganhou")
elif computador == 1 :# PAPEL
   if player == 0 :
    print ("Computador Ganhou")
   elif player == 1 :
    print("EMPATE")
   elif player ==2 :
    print("Jogador Ganhou")
elif computador == 2 :# TESOURA
   if player == 0 :
    print("Jogador Ganhou")
   elif player == 1 :
    print("Computador Ganhou")
   elif player ==2 :
    print ("EMPATE")