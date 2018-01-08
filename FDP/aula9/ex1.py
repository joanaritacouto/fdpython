fin = open('nums.txt')

sum = 0

def soma(sum):
	for i in fin:
		i= float(i)
		sum += i
	return sum

print (soma(sum))