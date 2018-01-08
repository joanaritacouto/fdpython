#encoding:utf8

l=float(input("Largura= "))
c=float(input("Comprimento= "))

a=l*c
p=2*l + 2*c

print("area= " +  str(a) + " m2" + " e o perimetro= "  + str(p)  + " m.")
print(" A área é {:.2f} m² e o perímetro é {:.2f} m.".format(a,p))



print("-------------------------------------------------------------------------")
print("|			|			|			|")
print("|      Largura		|    Comprimento        |	                |")
print("|			|			|			|")
print("-------------------------------------------------------------------------")
print("|			|			|			|")
print("|	{}		|	 {}		|	 {}		|".format(l,c,a))
print("|			|			|			|")
print("-------------------------------------------------------------------------")
print("|			|			|			|")
print("|	{}		|	 {}		|	 {}		|".format(l,c,p))
print("|			|			|			|")
print("-------------------------------------------------------------------------")
