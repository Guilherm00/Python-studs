#financiamento de casa
val_casa = float(input("Qual o valor da casa desejada?"))
salario = float(input("Qual seu salário atual ?"))
anos = int (input("Em quantos anos pretende pagar?"))

val_parc = val_casa / (anos * 12) 

print("O valor da mensalidade para uma casa no valor de R${:.3f} é R${:.3f}".format(val_casa, anos))

if val_parc <= 0.3* salario :
  print("Você esta apto a fazer o financiamento")
else:
 print ("Infelizmente você não está apto a fazer o financiamento FINANCIAMENTO NEGADO")
