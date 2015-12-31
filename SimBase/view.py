import math
from tkinter import *

from .shipController import HumanShipController

class WindowManager:
	def __init__(self):
		self.root = Tk()
		self.root.title("Neural Net Hunger Games")
		self.root.resizable(width=FALSE, height=FALSE)
		self.root.geometry("1280x720")
		self.canvas = Canvas(self.root, width=1280, height=720, background="black")
		self.canvas.pack()
	def clear(self):
		self.canvas.delete("all")
	def transformPoint(self, x, y):
		return x + 640, -y + 360;
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
	def bindArrowKeys(self, upFcn = None, downFcn = None, leftFcn = None, rightFcn = None):
		if upFcn != None:
			self.root.bind("<Up>", lambda event: upFcn(True))
			self.root.bind("<KeyRelease-Up>", lambda event: upFcn(False))
		if downFcn != None:
			self.root.bind("<Down>", lambda event: downFcn(True))
			self.root.bind("<KeyRelease-Down>", lambda event: downFcn(False))
		if leftFcn != None:
			self.root.bind("<Left>", lambda event: leftFcn(True))
			self.root.bind("<KeyRelease-Left>", lambda event: leftFcn(False))
		if rightFcn != None:
			self.root.bind("<Right>", lambda event: rightFcn(True))
			self.root.bind("<KeyRelease-Right>", lambda event: rightFcn(False))
	def executeFrameEvent(self):
		self.frameEvent()
		self.root.after(16, self.executeFrameEvent)
	def mainloop(self, frameEvent):
		self.frameEvent = frameEvent
		self.root.bind("<q>", lambda event: self.root.destroy())
		self.root.after(1, self.executeFrameEvent)
		self.root.mainloop()

class SimView(WindowManager):
	def __init__(self, model):
		WindowManager.__init__(self)
		self.model = model
	def frame(self):
		self.clear()
		for ship in self.model.ships:
			self.drawShip(ship)
	def drawShip(self, ship):
		self.drawLine(
			ship.x,
			ship.y,
			ship.x + 8 * math.cos(ship.rotation + 4 * math.pi / 3),
			ship.y + 8 * math.sin(ship.rotation + 4 * math.pi / 3))
		self.drawLine(
			ship.x,
			ship.y,
			ship.x + 8 * math.cos(ship.rotation - 4 * math.pi / 3),
			ship.y + 8 * math.sin(ship.rotation - 4 * math.pi / 3))
		self.drawLine(
			ship.x + 12 * math.cos(ship.rotation),
			ship.y + 12 * math.sin(ship.rotation),
			ship.x + 8 * math.cos(ship.rotation + 4 * math.pi / 3),
			ship.y + 8 * math.sin(ship.rotation + 4 * math.pi / 3))
		self.drawLine(
			ship.x + 12 * math.cos(ship.rotation),
			ship.y + 12 * math.sin(ship.rotation),
			ship.x + 8 * math.cos(ship.rotation - 4 * math.pi / 3),
			ship.y + 8 * math.sin(ship.rotation - 4 * math.pi / 3))
	def generateController(self):
		controller = HumanShipController()
		self.bindArrowKeys(
			upFcn = controller.setForward,
			leftFcn = controller.setLeft,
			rightFcn = controller.setRight)
		return controller