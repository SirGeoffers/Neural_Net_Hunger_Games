from model import SimModel
from view import SimView
import time

model = SimModel()
view = SimView(model)

for i in range(10):
	ship = model.addShip()
	ship.setTurn(0.1)
	ship.setThrottle(0.01)

while view.alive():
	time.sleep(0.01)
	model.frame()