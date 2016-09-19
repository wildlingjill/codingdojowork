class MathDojo(object):
	def __init__(self):
		self.result = 0

	def add(self, *otherNumbers):
		for i in otherNumbers:
			if type(i) == list or type(i) == tuple:
				for number in i:
					self.result += number
			else:
				self.result += i
		return self

	def subtract(self, *otherNumbers):
		for i in otherNumbers:
			if type(i) == list or type(i) == tuple:
				for number in i:
					self.result -= number
			else:
				self.result -= i
		return self


md = MathDojo()
print md.add(2).add(2,5).subtract(3,2).result

md2 = MathDojo()
print md2.add([1],3,4).add([3, 5, 7, 8], (2, 4.3, 1.25)).subtract(2, [2,3], [1.1, 2.3]).result