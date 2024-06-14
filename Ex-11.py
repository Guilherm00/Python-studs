a = float(input("Qual a altura ?: "))
l = float(input("Qual a largura?: "))
tinta = (a*l)/ 2
print("A sua parede tem a dimensão de {}x{} e a área de {}m² \n Para pintar sua parede é preciso de {} litros de tinta. ".format(a,l,(a*l),tinta))