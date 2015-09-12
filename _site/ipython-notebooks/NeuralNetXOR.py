import numpy as np
import math

X = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])
y = np.array([[0, 1, 1, 0]]).T
init_theta = 2*np.random.random((13,1)) - 1

def runForward(X, theta):
	theta1 = np.array(theta[:9]).reshape(3,3)
	theta2 = np.array(theta[9:]).reshape(4,1)
	h1 = sigmoid(np.dot(X, theta1)) #4x3 * 3x3 = 4x3
	h1_bias = np.insert(h1, 3, [1,1,1,1], axis=1)
	output = sigmoid(np.dot(h1_bias, theta2)) #4x4 * 4x1 = 4x1
	return output
	#4x3 * 3x1 = 4x1
def costFunction(X, y, theta):
	m = float(len(X))
	hThetaX = np.array(runForward(X, theta))
	return np.sum(np.abs(y - hThetaX))
def sigmoid(x): return 1 / (1 + np.exp(- x))

def demoRun():
	print("Random theta: \n%s\n" % (runForward(X, init_theta)))
	print("Cost: %s\n" % (costFunction(X,y, init_theta)))
	theta = np.array([[-10.27649069,-14.03, 10.45888659, 9.12 ,14.87, -21.50294038, 1.85, -13.28, -0.15360052, -11.21345025, 35.77912716, 11.05, -2.49589577]])
	print("Optimal theta: \n%s\n" % (runForward(X, theta)))
	print("Cost: %s\n" % (costFunction(X, y, theta)))