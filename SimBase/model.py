import math
import random

MAX_THRUST = 0.2
MAX_TURN = 0.2

def clip(min, x, max):
	if x < min:
		return min
	elif x > max:
		return max
	else:
		return x

class Ship:
	def __init__(self, x=0, y=0, rotation=0):
		# physical state
		self.x = x
		self.y = y
		self.rotation = rotation
		self.vx = 0
		self.vy = 0
		# control state
		self.turn = 0 # range: [-1 - 1]
		self.throttle = 0 # range: [0 - 1]
	def setTurn(self, turn):
		self.turn = clip(-1, turn, 1)
	def setThrottle(self, throttle):
		self.throttle = clip(0, throttle, 1)
	def applyTurn(self):
		self.rotation += MAX_TURN * self.turn
	def applyThrust(self):
		self.vx += MAX_THRUST * self.throttle * math.cos(self.rotation)
		self.vy += MAX_THRUST * self.throttle * math.sin(self.rotation)
	def applyVelocity(self):
		self.x += self.vx
		self.y += self.vy
	def frame(self):
		self.applyTurn()
		self.applyThrust()
		self.applyVelocity()

class SimModel:
	def __init__(self):
		self.ships = []
	def addShip(self):
		newShip = Ship(rotation = random.uniform(0, 2 * math.pi))
		self.ships.append(newShip)
		return newShip
	def frame(self):
		for ship in self.ships:
			ship.frame()