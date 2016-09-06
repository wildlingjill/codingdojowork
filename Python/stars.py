#part 1 

x = [4, 6, 1, 3, 5, 7, 25]

def draw_stars(list):
	for item in list:
		print "*" * item

draw_stars(x)

#part 2

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars(list):
	for item in list:
		if type(item) == str:
			print item[0].lower() * len(item)
		else:
			print "*" * item

draw_stars(x) 