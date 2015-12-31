class ShipController:
	def __init__(self, ship=None):
		if ship != None:
			self.setShip(ship)
	def setShip(self, ship):
		self.ship = ship
	def setThrottle(self, throttle):
		if self.ship != None:
			self.ship.setThrottle(throttle)
	def setTurn(self, turn):
		if self.ship != None:
			self.ship.setTurn(turn)

class HumanShipController:
	def __init__(self, ship=None):
		self.controller = ShipController(ship)
		self.forward = False
		self.left = False
		self.right = False
	def setShip(self, ship):
		self.controller.setShip(ship)
	def setForward(self, forward):
		self.forward = forward
		if self.forward:
			self.controller.setThrottle(1)
		else:
			self.controller.setThrottle(0)
	def updateTurn(self):
		turn = 0
		if self.left:
			turn += 1
		if self.right:
			turn -= 1
		self.controller.setTurn(turn)
	def setLeft(self, left):
		self.left = left
		self.updateTurn()
	def setRight(self, right):
		self.right = right
		self.updateTurn()