metros = float(input("Quantos metros você deseja converter?: "))
cm = metros / 100 * 10
print ("{} metros em centímetros é {:,.3f} e em milimetros é {:,.3f}".format(metros,cm,(cm*10)))
