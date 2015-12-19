
import random

class Perceptron:

	def __init__(self, prevPerceptrons):
		self.prevPerceptrons = prevPerceptrons
		self.value = 0
		self.weights = []
		for i in range(len(self.prevPerceptrons)):
			weightValue = random.uniform(-1, 1)
			self.weights.append(weightValue)

	def setWeight(self, index, value):
		self.weights[index] = value

	def setValue(self, newValue):
		self.value = newValue

	def getValue(self):
		return self.value

	def calcValue(self):
		out = 0
		for i in range(len(self.prevPerceptrons)):
			out += self.prevPerceptrons[i].getValue() * self.weights[i]
		return out

	def calcAndSetValue(self):
		self.setValue(self.calcValue())

class NeuralNet:

	def __init__(self, layerSizes):
		self.layers = []
		prevLayer = []
		for i in layerSizes:
			newLayer = self.createLayer(i, prevLayer)
			self.layers.append(newLayer)
			prevLayer = newLayer

	def createLayer(self, size, prevLayer):
		layer = []
		for i in range(size):
			newPerceptron = Perceptron(prevLayer)
			layer.append(newPerceptron)
		return layer

	def setInput(self, newInputs):
		if len(newInputs) != len(self.layers[0]):
			print("Invalid number of inputs")
			return False
		for i in range(len(self.layers[0])):
			self.layers[0][i].setValue(newInputs[i])
		return True

	def run(self):
		for i in range(1, len(self.layers)):
			for j in self.layers[i]:
				j.calcAndSetValue()
		out = []
		for i in self.layers[-1]:
			out.append(i.getValue())
		return out

	def runWithInput(self, newInputs):
		if (self.setInput(newInputs)):
			return self.run()
		return []

if __name__ == "__main__":

	print("Testing neural nets\n");

	net = NeuralNet([2, 1])
	output = net.runWithInput([1, 0.5])
	print(output)