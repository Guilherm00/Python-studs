salario =  float(input("Informe o salário?: "))
aumento = salario *(15/100)
print ("Salário base R${:,.2f}. Salário com aumento R${:,.2f}".format(salario,(salario+aumento)))
print ("o seu aumento foi de R${:,.2f}".format(aumento))