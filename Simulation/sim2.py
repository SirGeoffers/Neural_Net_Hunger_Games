from SimBase.simBase import SimBase
from SimBase.shipController import ShipController
from Net.main import NeuralNet

class DroneShipController:
	def __init__(self, ship=None, baseNet=None):
		self.ship = ship
		self.controller = ShipController(ship)
		if baseNet != None:
			self.net = baseNet.clone()
			self.net.mutate()
		else:
			self.net = NeuralNet([1, 3, 2])
	def setShip(self, ship):
		self.controller.setShip(ship)
	def frame(self):
		# input environment data to net, set controls with output
		output = self.net.runWithInput([self.ship.rotation])
		self.controller.setThrottle(output[0])
		self.controller.setTurn(2 * output[1] - 1)

class Sim2(SimBase):
	def __init__(self, numShips=0):
		SimBase.__init__(self)
		self.numShips = numShips
	def setup(self):
		humanShip = sim.model.addShip()
		self.humanController = sim.view.generateController()
		self.humanController.setShip(humanShip)
		self.droneControllers = []
		for i in range(self.numShips):
			droneShip = sim.model.addShip()
			droneController = DroneShipController(droneShip)
			self.droneControllers.append(droneController)
	def controlFrame(self):
		for droneController in self.droneControllers:
			droneController.frame()

sim = Sim2(10)
sim.run()