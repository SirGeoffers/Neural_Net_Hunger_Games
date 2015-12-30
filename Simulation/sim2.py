from SimBase.simBase import SimBase
from SimBase.shipController import ShipController

sim = SimBase()

humanShip = sim.model.addShip()
humanController = sim.view.generateController()
humanController.setShip(humanShip)

droneShip = sim.model.addShip()
droneController = ShipController(droneShip)
droneController.setThrottle(0.5)
droneController.setTurn(-0.5)

sim.run()