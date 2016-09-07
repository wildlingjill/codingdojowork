import random

head_count = 0
tail_count = 0

for number in range (1, 5000):
	random_num = round(random.random())
	if random_num == 1:
		coin = "head"
		head_count += 1
		print "Attempt #%d: Throwing a coin...It's a %s! Got %d head(s) so far and %d tail(s) so far" %(number, coin, head_count, tail_count)
	else:
		coin = "tail"
		tail_count += 1
		print "Attempt #%d: Throwing a coin...It's a %s! Got %d head(s) so far and %d tail(s) so far" %(number, coin, head_count, tail_count)