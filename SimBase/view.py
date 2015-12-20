import math
import threading
from tkinter import *

class Pen:
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
			fill="0x00ff00")

class WindowManager:
	def __init__(self, model):
		self.model = model
		self.root = Tk()
		self.root.title("Neural Net Hunger Games")
		self.root.resizable(width=FALSE, height=FALSE)
		self.root.geometry("1280x720")
		self.canvas = Canvas(self.root, width=1280, height=720, background="black")
		self.canvas.pack()
		self.pen = Pen(self.canvas)
		self.root.after(1, self.frame)
		self.root.mainloop()
	def frame(self):
		self.pen.clear()
		for ship in self.model.ships:
			self.drawShip(ship)
		self.root.after(17, self.frame) # ~60 fps
	def drawShip(self, ship):
		self.pen.drawLine(
			ship.x,
			ship.y,
			ship.x + 4 * math.cos(ship.rotation + 4 * math.pi / 3),
			ship.y + 4 * math.sin(ship.rotation + 4 * math.pi / 3))
		self.pen.drawLine(
			ship.x,
			ship.y,
			ship.x + 4 * math.cos(ship.rotation - 4 * math.pi / 3),
			ship.y + 4 * math.sin(ship.rotation - 4 * math.pi / 3))
		self.pen.drawLine(
			ship.x + 6 * math.cos(ship.rotation),
			ship.y + 6 * math.sin(ship.rotation),
			ship.x + 4 * math.cos(ship.rotation + 4 * math.pi / 3),
			ship.y + 4 * math.sin(ship.rotation + 4 * math.pi / 3))
		self.pen.drawLine(
			ship.x + 6 * math.cos(ship.rotation),
			ship.y + 6 * math.sin(ship.rotation),
			ship.x + 4 * math.cos(ship.rotation - 4 * math.pi / 3),
			ship.y + 4 * math.sin(ship.rotation - 4 * math.pi / 3))
		
		#self.pen.drawCircle(ship.x, ship.y, 5)
		#self.pen.drawLine(
		#	ship.x,
		#	ship.y,
		#	ship.x + 10 * math.cos(ship.rotation),
		#	ship.y + 10 * math.sin(ship.rotation))

class SimView(threading.Thread):
	def __init__(self, model):
		threading.Thread.__init__(self)
		self.daemon = True
		self.model = model
		self.isAlive = True
		self.start()
	def run(self):
		wm = WindowManager(self.model)
		self.isAlive = False
	def alive(self):
		return self.isAlive