
#Part 1 - create a program that prints all the odd numbers from 1 to 1000, use a for loop and not an array.

for number in range(1, 1000):
	if number % 2 == 1:
		print number
	else:
		continue


#Part 2 - create another program that prints all the multiples of 5 from 5 to 1000000.

for number in range(5, 1000000):
	if number % 5 == 0:
		print number
	else:
		continue