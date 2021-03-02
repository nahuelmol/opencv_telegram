import numpy as np 

X =[[1,2,3,2.5],
	[2.0,5.0,-1.0,2.0],
	[-1.5,2.7,3.3,-0.8]] 

class layer_creator:

	def __init__(self,n_inputs,n_neurons):
		self.weights = 0.10 *np.random.randn(n_inputs,n_neurons)
		self.biases = np.zeros((1,n_neurons))
	def get_output(self,inputs):
		self.output = np.dot(inputs,self.weights) + self.biases

layer1 = layer_creator(4,5)
layer2 = layer_creator(5,2)

layer1.get_output(X)
output = layer1.output
layer2.get_output(output)

print(layer2.output)