from humans_oop import Human

class Wizard(Human):
	def heal(self):
		self.health += 10
class Ninja(Human):
	def steal(self):
		self.stealth += 5
class Samurai(Human):
	def sacrifice(self):
		self.health -= 5


harry = Wizard()
rain = Ninja()
tom = Samurai()

print harry.health
print rain.health
print tom.health


harry.heal()
print harry.health

rain.steal()
print rain.stealth

tom.sacrifice()
print tom.health
print tom.stealth



"""class Parent(object): # inherits from the object class
  # parent methods and attributes here
class Child(Parent): #inherits from Parent class so we define Parent as the first parameter
  # parent methods and attributes are implicitly inherited
  # child methods and attributes


  from human import Human
class Wizard(Human):
    def __init__(self):
        super(Wizard, self).__init__()   # use super to call the Human __init__ method
        self.intelligence = 10           # every wizard starts off with 10 intelligence
    def heal(self):
        self.health += 10
class Ninja(Human):
    def __init__(self):
        super(Ninja, self).__init__()    # use super to call the Human __init__ method
        self.stealth = 10                # every Ninja starts off with 10 stealth
    def steal(self):
        self.stealth += 5
class Samurai(Human):
    def __init__(self):
        super(Samurai, self).__init__()  # use super to call the Human __init__ method
        self.strength = 10               # every Samurai starts off with 10 strength
    def sacrifice(self):
        self.health -= 5"""