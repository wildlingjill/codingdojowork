class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0 

# display price, max speed and total miles
	def displayInfo(self):
		print self.price, self.max_speed, self.miles
		return self
	
# display "riding" and increase miles by 10
	def ride(self):
		self.miles += 10 
		print "Riding"
		return self

# display "reversing" and decrease miles by 5
	def reverse(self):
		if self.miles == 0:
			print "Can't reverse any further!"
			return self
		else:
			self.miles -= 5 
			print "Reversing"
			return self


bike1 = Bike(200, "25mph")
bike1.ride().ride().ride().reverse().displayInfo()


bike2 = Bike(150, "20mph")
bike2.ride().ride().reverse().reverse().displayInfo()


bike3 = Bike(175, "15mph")
bike3.reverse().reverse().reverse().displayInfo()