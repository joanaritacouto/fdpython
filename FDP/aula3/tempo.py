x = float( input('tempo em segundos: '))

y = x//3600

z = (x%3600)//60

w = x- 60*z - 3600*y

print(y,' :', z, ' :', w, ' ')

