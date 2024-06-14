diaria = int(input("Quantos dias de aluguel?:"))
km = float(input("Quantos kilometros foram rodados?: "))
preco = (60 * diaria) + (km * 0.15)
print ("Seu aluguel de {} dias e com a kilometragem de {}km ficou no total de R${:,.2f}".format(diaria,km,preco))