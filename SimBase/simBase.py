from .model import SimModel
from .view import SimView

class SimBase:
	def run(self):
		self.model = SimModel()
		self.view = SimView(self.model)
		self.setup()
		self.view.mainloop(self.simFrame)
	def simFrame(self):
		self.controlFrame()
		self.model.frame()
		self.view.frame()
	def setup(self):
		# called during setup
		# initialize ships/controllers/other objects here
		pass
	def controlFrame(self):
		# called every frame before physics are applied
		pass
