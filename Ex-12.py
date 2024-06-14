print ("=-=-=-=-=-=-=-=-=PROGRAMA DE DESCONTO=-=-=-=-=-=-=-=-=")
v = float(input("Qual valor da sua compra?: "))
d = v * 5 / 100
print ("O valor com 5% de desconto é R${:,.2f}".format(v-d))
