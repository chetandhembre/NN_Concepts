#loss Graph https://dl.dropboxusercontent.com/u/47591917/xor_loss.png

import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

xor = np.array([
  [0, 0, 0],
  [0, 1, 1],
  [1, 0, 1],
  [1, 1, 0]
])

learning_rate = 0.01

w1 = np.random.randn(2, 3)
b1 = np.random.randn(3, 1)

w2 = np.random.randn(3, 2)
b2 = np.random.randn(2, 1)

def softmax(x, y):
  probs = np.exp(x - np.max(x, axis=0))
  probs /= np.sum(probs)
  loss = -np.sum(np.log(probs[y]))
  return loss


def softmax_grad(x, y):
  probs = np.exp(x - np.max(x, axis=0))
  probs /= np.sum(probs)
  probs[y] -= 1
  probs /= 1
  return probs

def sigmoid(z):
  return 1.0/(1.0+np.exp(-z))

def sigmoid_prime(z):
    """Derivative of the sigmoid function."""
    return sigmoid(z)*(1-sigmoid(z))

input_sequence = np.random.randint(4, size=200000)
i = 0

loss = []
loss_record = []
x1 = []
x2 = []
h1_0 = []
h1_1 = []
h1_2 = []
output = []
while i < len(input_sequence):
  seq = input_sequence[i]
  row = xor[seq]
  _input = row[0: 2].reshape(2, 1)
  _output = row[2].reshape(1, 1)
  
  
  # input 2x1,  2 * 3
  # output 3x1
  h1 = np.transpose(w1).dot(_input) + b1
  
  h1_sig = sigmoid(h1)
  
  # input 3x1, 3x2
  # output 2x1
  h2 = np.transpose(w2).dot(h1_sig) + b2

  #loss
  loss.append(softmax(h2, _output))
  if i % 1000 == 0:
    print loss[-1]
    loss_record.append(loss[-1])
    x1.append(_input[0][0])
    x2.append(_input[1][0])
    h1_0.append(h1[0][0])
    h1_1.append(h1[1][0])
    h1_2.append(h1[2][0])
    output.append(np.max(h2))

  dscore = softmax_grad(h2, _output)

  # backpropagation
  # input 2x1, 3x1
  # output 3x1
  dw2 = h1_sig.dot(np.transpose(dscore))

  #input 1x1
  # output 1x1
  db2 = dscore

  # input 3x1, 1x1
  # output 3x1
  dh1_sig = w2.dot(dscore)

  dh1 = dh1_sig * sigmoid_prime(h1)

  #input 3x1, 2x1
  #output 2x3
  dw1 = _input.dot(np.transpose(dh1))
  
  #input 3x1
  db1 = dh1

  w1 = w1 - learning_rate * dw1
  b1 = b1 - learning_rate * db1

  w2 = w2 - learning_rate * dw2
  b2 = b2 - learning_rate * db2

  i = i + 1


print '********************* Testing *********** '
input_sequence = np.random.randint(4, size=50000)
i = 0
x1 = []
x2 = []
h1_0 = []
h1_1 = []
h1_2 = []
output = []
colors = []

while i < len(input_sequence):
  seq = input_sequence[i]
  row = xor[seq]
  _input = row[0: 2].reshape(2, 1)
  _output = row[2].reshape(1, 1)
  
  h1 = np.transpose(w1).dot([[0], [0]]) + b1
  h1_sig = sigmoid(h1)
  h2 = np.transpose(w2).dot(h1_sig) + b2
  
  if i % 1000 == 0:
    x1.append(_input[0][0])
    x2.append(_input[1][0])
    output.append(np.max(h2))
    colors.append(_output[0][0])
  i = i + 1

plt.plot(loss_record)
plt.ylabel('Loss')
plt.xlabel('Iterations (sampled per 1000 interation)')
plt.savefig('xor_loss.png')
plt.show()
