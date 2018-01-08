
# This program should find the phase of a fictional substance
# for given temperature and pressure conditions, but it has several bugs!
# 
# a) Try to run the program with Python3 and see what happens.
#    There's a syntax error near the end.  Fix it.
# b) Try again.  It'll crash with a runtime error.  Find the cause and fix it.
# c) There is also a semantic error: for T=300 and P=100, phase should be SOLID.
#    Fix it to agree with the phase diagram.  Test in several conditions!
# d) Adjust the format string to output temperature with 1 decimal place
#    and pressure with 3. 

print("Kryptonite phase classifier")

# Input.  (You can fix the runtime error by changing something here!)
T = float(input("Temperature (K)? "))
P = float(input("Pressure (kPa)? "))

# Determine the phase. (This is wrong! Fix to match phase diagram.)

#if P == 0 or T == 0: 
#    print("Error: Neither temperature or pressure can be zero")
#    exit(1)
#if P+T==0 :    
#    phase = "SOLID"
#if P == 0 and T > 0:
#    phase = "GAS"
if (P > 50.0 and T <= 400.0) or (T/P<=8) :
    phase = "SOLID"
elif T > 400.0 and P > 50:
    phase = "LIQUID"
else:
    phase = "GAS"

# Output.  (There's a subtle syntax error here!)
#P = round(P,3)
#T = round(T,1)
print("At {} K and {} kPa, Kryptonite is in the {} phase.".format(round(T,1), round(P,3), phase))