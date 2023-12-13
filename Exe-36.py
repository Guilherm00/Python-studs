#financiamento de casa 
val_casa = float(input("Qual o valor da casa desejada?"))
salario = float(input("Qual seu salário atual ?"))
meses = int (input("Em quantos anos pretende pagar?"))

val_parc = val_casa / meses

print("O valor da mensalidade é :")
print(val_parc)

if val_parc <= 0.3* salario :
  print("Você esta apto a fazer o financiamento")
else:
 print ("Infelizmente você não está apto a fazer o financiamento FINANCIAMENTO NEGADO")