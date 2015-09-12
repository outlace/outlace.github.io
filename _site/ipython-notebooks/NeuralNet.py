import numpy as np
import math

X = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1], [1,0,1], [0,0,1], [0,1,1] ])
y = np.array([[0,0,1,1, 1, 0, 0]]).T
syn0 = 2*np.random.random((3,1)) - 1

def runForward(X, theta):
	return sigmoid(np.dot(X, theta))
	#4x3 * 3x1 = 4x1
def costFunction(X, y, theta):
	m = float(len(X))
	hThetaX = np.array(runForward(X, theta))
	return np.sum(np.abs(y - hThetaX))
def sigmoid(x): return 1 / (1 + np.exp(- x))

def demoRun():
	print("Random theta: \n%s\n" % (runForward(X, syn0)))
	print("Cost: %s\n" % (costFunction(X,y,syn0)))
	#these "optimal" theta values we're calculated from gradient descent
	theta = np.array([[ 9.67299303],[-0.2078435],[-4.62963669]])
	print("Optimal theta: \n%s\n" % (runForward(X, theta)))
	print("Cost: %s\n" % (costFunction(X, y, theta)))

#demoRun()