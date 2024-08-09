import math
print("-="*7+"SCT"+"-="*7)
angulo =  float(input("Informe o ângulo:"))
seno = math.sin(math.radians(angulo))
coss = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print ("Com o andulo de {}º \n seu seno é {:.2f} \n seu cosseno é {:.2f} \n e sua tangente é {:.2f} ".format(angulo,seno,coss,tan))