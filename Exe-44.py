#Gerenciamento de pagamentos
preco = float (input("Informe o valor a ser pago:"))
print (''''Formas de pagamento:
[1] Á vista dinheiro
[2] Á vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão ''''')
opcao = int (input("Escolha uma Opção: "))

if opcao == 1 :
    total = preco - (preco * 10/100)
    print ("A sua compra foi de R${:.2f}. Valor final R${:.2f} ".format(preco, total))
elif opcao == 2 :
   total = preco - (preco * 5/100)
   print ("A sua compra foi de R${:.2f}. Valor final R${:.2f} ".format(preco, total))
elif opcao == 3:
  total = preco / 2
  print ("Sua parcela será de {:.2f} ".format(total))
  print ("A sua compra de R${:.2f} Valor final R${:.2f} ".format(preco, preco))
elif opcao == 4 :
  total = preco + (preco * 20/100)
  total_parcela = int (input("Em quantas parcelas será feito o pagamento? "))
  parcela = total / total_parcela
  print("sua compra parcelada em {}x de {:.2f} COM JUROS".format(total_parcela, parcela))
  print ("sua compra no valor de {:.2f} com juros ficou R${:.2f}. ".format(preco,total))
else:
  ("Opção inválida por favor escolha uma opção válida.")

