x= int ( input ('numero 1: '))
y= int ( input ('numero 2: '))
z= int ( input ('numero 3: '))

if x < y and z < y :
 print ('numero maior ', y)

elif x > y and x > z :
 print ('numero maior ', x)

elif z > x and z > y :
 print ('numero maior ', z)

elif x == y and x > z :
 print ('numero maior ', x)

elif x == y and x < z :
 print ('numero maior ', z)

elif x == z and x > y :
 print ('numero maior ', x)

elif x == z and x < y : 
 print ('numero maior ', y)

elif z == y and z > x :
 print ('numero maior ', z)

elif z == y and z < x :
 print ('numero maior ', x)

elif x == y == z : 
 print ('igual ',x)
 



