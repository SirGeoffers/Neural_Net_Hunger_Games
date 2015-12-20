from model import SimModel
from view import SimView
import time

model = SimModel()
view = SimView(model)

ship = model.addShip()
view.getController().setShip(ship)

while view.alive():
	time.sleep(0.01)
	model.frame()