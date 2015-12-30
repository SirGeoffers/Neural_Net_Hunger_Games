from .model import SimModel
from .view import SimView

class SimBase:
	def __init__(self):
		self.model = SimModel()
		self.view = SimView(self.model)
	def run(self):
		self.view.mainloop(self.simFrame)
	def simFrame(self):
		self.model.frame()
		self.view.frame()
