
import math
import random

def sigmoid(value):
	if value > 100:
		value = 100
	elif value < -100:
		value = -100
	return 1 / (1 + math.e**(-value))

class Perceptron:

	def __init__(self, prevPerceptrons):
		self.prevPerceptrons = prevPerceptrons
		self.value = 0
		self.weights = []
		for i in range(len(self.prevPerceptrons)):
			weightValue = random.uniform(-1, 1)
			self.weights.append(weightValue)

	def getWeight(self, index):
		return self.weights[index]

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
		return sigmoid(out)

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

	def mutate(self, mutationProbability):
		for layer in self.layers:
			for perceptron in layer:
				for w in range(len(perceptron.weights)):
					if (random.random() < mutationProbability):
						perceptron.weights[w] = random.uniform(-1, 1)

	def clone(self):
		layerSizes = []
		for layer in self.layers:
			layerSizes.append(len(layer))
		newNet = NeuralNet(layerSizes)
		for layerIndex in range(len(self.layers)):
			oldLayer = self.layers[layerIndex]
			newLayer = newNet.layers[layerIndex]
			for perceptronIndex in range(len(oldLayer)):
				oldPerceptron = oldLayer[perceptronIndex]
				newPerceptron = newLayer[perceptronIndex]
				for weightIndex in range(len(oldPerceptron.weights)):
					oldWeight = oldPerceptron.getWeight(weightIndex)
					newPerceptron.setWeight(weightIndex, oldWeight)
		return newNet


if __name__ == "__main__":

	print("Testing neural nets");

	net1 = NeuralNet([2, 1])
	output = net1.runWithInput([1, 0.5])
	print("Net 1:", id(net1), output)

	net2 = NeuralNet([2, 1])
	output = net2.runWithInput([1, 0.5])
	print("Net 2:", id(net2), output)

	print("Mutating Net 2")
	net2.mutate(1)

	output = net2.runWithInput([1, 0.5])
	print("Net 2:", id(net2), output)

	print("Cloning Net 2 to Net 3")
	clonedNet = net2.clone()

	output = clonedNet.runWithInput([1, 0.5])
	print("Net 3:", id(clonedNet), output)