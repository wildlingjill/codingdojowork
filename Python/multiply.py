a = [2,4,10,16] 

def multiply(list, n):
	c = []
	for item in list:
		c.append(item*5)
	return c

b = multiply(a, 5)
print b