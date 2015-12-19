from tkinter import *

from model import SimModel
from view import SimView

root = Tk()
root.title("Neural Net Hunger Games")
root.resizable(width=FALSE, height=FALSE)
root.geometry("1280x720")

canvas = Canvas(root, width=1280, height=720, background="black")
canvas.pack()

model = SimModel()
view = SimView(canvas, model)

for i in range(10):
	ship = model.addShip()
	ship.setTurn(1)
	ship.setThrottle(1)

def tick():
	model.frame()
	view.frame()
	root.after(20, tick) # 50 fps

root.after(1, tick)
root.mainloop()