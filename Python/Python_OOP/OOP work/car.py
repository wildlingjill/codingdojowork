class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.speed = speed 
		self.fuel = fuel
		self.mileage = mileage
		self.price = price
		if price > 10000:
			self.tax = .15
		else:
			self.tax = .12
		self.display_all()

	def display_all(self):
		print 'Price: ' + str(self.price)
		print 'Speed: ' + str(self.speed) + 'mph'
		print 'Fuel: ' + self.fuel
		print 'Mileage: ' + str(self.mileage) + 'mpg'
		print 'Tax: ' + str(self.tax)



'''
class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.speed = speed 
		self.fuel = fuel
		self.mileage = mileage
		self.price = price
		if price > 10000:
		   self.tax = .15
		else:
			self.tax = .12
		self.display_all()

	def display_all(self):
		print 'Price: ' + str(self.price)
		print 'Speed: ' + str(self.speed) + 'mph'
		print 'Fuel: ' + self.fuel
		print 'Mileage: ' + str(self.mileage) + 'mpg'
		print 'Tax: ' + str(self.tax)
'''




car1 = Car(1000, 60, "Full", "20mpg")
car2 = Car(10000, 150, "Full", "30mpg")
car3 = Car(5000, 90, "Not Full", "15mpg")
car4 = Car(2000, 80, "Full", "25mpg")
car5 = Car(7500, 100, "Not Full", "35mpg")
car6 = Car(800, 50, "Not Full", "15mpg")

	
