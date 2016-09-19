class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0 

# display price, max speed and total miles
	def displayInfo(self):
		print self.price, self.max_speed, self.miles
	
# display "riding" and increase miles by 10
	def ride(self):
		self.miles += 10 
		print "Riding"

# display "reversing" and decrease miles by 5
	def reverse(self):
		if self.miles == 0:
			print "Can't reverse any further!"
		else:
			self.miles -= 5 
			print "Reversing"


bike1 = Bike(200, "25mph")
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()


bike2 = Bike(150, "20mph")
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()


bike3 = Bike(175, "15mph")
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()