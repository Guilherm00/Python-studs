print ("=-=-=-=-=-=-=-=-=PROGRAMA DE CONVERSÃO=-=-=-=-=-=-=-=-=")
n = float(input("Qual o seu saldo disponível?:"))
saldo_em_dolar = n / 5.36
print ("Com seu saldo de R${:,.2f} em dolares é U${:,.2f}".format(n,saldo_em_dolar))