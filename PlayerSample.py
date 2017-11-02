	
class Player:
	name = "name"
	health = 20
	damage = 5
	speed = 5
	
	def __init__(self, name):
		self.name = name
	
	def increase_speed(self, amount):
		self.speed += amount
		
	def decrease_speed(self, amount):
		self.speed -= amount
		
	def print_speed(self):
		print (self.name + " " + str(self.speed))
		

player1 = Player("Charlie")
player2 = Player("Trevor")

player1.increase_speed(2)

player2.decrease_speed(2)

player1.print_speed()

player2.print_speed()
