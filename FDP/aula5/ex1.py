
def imc(p, a):
 imc= p/(a**2)
 return imc

p = float(input('peso: '))
a = float(input('altura: '))

z=imc(p, a)
print('IMC: ', z)
