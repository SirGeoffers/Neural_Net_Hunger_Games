from .model import SimModel
from .view import SimView

class SimBase:
	def run(self):
		self.speedup = 1
		self.model = SimModel()
		self.view = SimView(self.model)
		self.view.bindSpaceKey(self.setFastMode)
		self.setup()
		self.view.mainloop(self.simFrame)
	def setFastMode(self, fastMode):
		if fastMode:
			self.speedup = 10
		else:
			self.speedup = 1
	def simFrame(self):
		self.controlFrame()
		for i in range(self.speedup):
			self.model.frame()
		self.view.frame()
	def setup(self):
		# called during setup
		# initialize ships/controllers/other objects here
		pass
	def controlFrame(self):
		# called every frame before physics are applied
		pass
