from SimBase.model import SimModel
from SimBase.view import SimView
from SimBase.shipController import ShipController
from Net.main import NeuralNet
import math
import time
import random

class NetShipController:
	def __init__(self, ship=None, net=None):
		self.controller = ShipController(ship)
		self.ship = ship
		if net == None:
			self.net = NeuralNet([1, 3, 2])
		else:
			self.net = net
	def setShip(self, ship):
		self.ship = ship
	def frame(self):
		definiteAngleToCenter = math.atan2(-self.ship.y, -self.ship.x)
		currentFacingAngle = ((self.ship.rotation + math.pi) % (2 * math.pi)) - math.pi
		angleChange = (definiteAngleToCenter - currentFacingAngle + math.pi) % (2 * math.pi) - math.pi
		out = self.net.runWithInput([angleChange])
		self.controller.setThrottle(out[0])
		self.controller.setTurn(out[1] * 2 - 1)
	def cloneAndMutate(self, newShip):
		cloneNet = self.net.clone()
		cloneNet.mutate(0.1)
		return NetShipController(newShip, cloneNet)

model = SimModel()
view = SimView(model)

playerShip = model.addShip()
view.getController().setShip(playerShip)

def initShip(ship):
	ship.x = random.uniform(-50, 50)
	ship.y = random.uniform(-50, 50)
	ship.rotation = random.uniform(-math.pi, math.pi)

nControllers = []
for i in range(40):
	nShip = model.addShip()
	initShip(nShip)
	nController = NetShipController(nShip)
	nControllers.append(nController)

frameCount = 0

def doFrameNow():
	global frameCount
	global nControllers
	frameCount += 1
	if frameCount % 200 == 199:
		survivors = []
		numDead = 0
		for nController in nControllers:
			nShip = nController.ship
			if nShip.x > 200 or nShip.x < -200 or nShip.y > 200 or nShip.y < -200:
				numDead += 1
				model.removeShip(nShip)
			else:
				survivors.append(nController)
		nControllers = survivors[:] # clone survivors list
		for i in range(numDead):
			newShip = model.addShip()
			initShip(newShip)
			nController = random.choice(survivors).cloneAndMutate(newShip)
			nControllers.append(nController)
	for nController in nControllers:
		nController.frame()
	model.frame()

while view.alive():
	time.sleep(0.01)
	for i in range(50):
		doFrameNow()