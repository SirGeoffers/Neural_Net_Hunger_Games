import math

class SimDrawer:
	def __init__(self, canvas):
		self.canvas = canvas
	def clear(self):
		self.canvas.delete("all")
	def transformPoint(self, x, y):
		return x + 640, y + 360;
	def drawCircle(self, x, y, radius):
		x, y = self.transformPoint(x, y)
		self.canvas.create_oval(
			x - radius,
			y - radius,
			x + radius,
			y + radius,
			outline="white")
	def drawLine(self, x1, y1, x2, y2):
		x1, y1 = self.transformPoint(x1, y1)
		x2, y2 = self.transformPoint(x2, y2)
		self.canvas.create_line(
			x1,
			y1,
			x2,
			y2,
			fill="white")

class SimView:
	def __init__(self, canvas, model):
		self.model = model
		self.pen = SimDrawer(canvas)
	def frame(self):
		self.pen.clear()
		for ship in self.model.ships:
			self.drawShip(ship)
	def drawShip(self, ship):
		self.pen.drawCircle(ship.x, ship.y, 5)
		self.pen.drawLine(
			ship.x,
			ship.y,
			ship.x + 10 * math.cos(ship.rotation),
			ship.y + 10 * math.sin(ship.rotation))
		
