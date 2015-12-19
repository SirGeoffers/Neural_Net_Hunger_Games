from tkinter import *
import math
import time

root = Tk()
root.title("Neural Net Hunger Games")
root.resizable(width=FALSE, height=FALSE)
root.geometry("1280x720")

canvas = Canvas(root, width=1280, height=720, background="black")
canvas.pack()

def drawShip(x, y, rotation):
	canvas.create_oval(x - 5, y - 5, x + 5, y + 5, outline="white")
	canvas.create_line(x, y, x + 10 * math.cos(rotation), y + 10 * math.sin(rotation), fill="white")

sx = 100
sy = 100
sr = 1
def tick():
	global sx
	global sy
	global sr
	sr -= 0.01
	sx += 5 * math.cos(sr)
	sy += 5 * math.sin(sr)
	canvas.delete("all")
	drawShip(sx, sy, sr)
	root.after(10, tick)

root.after(1, tick)
root.mainloop()