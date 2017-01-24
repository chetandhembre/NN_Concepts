### Forward And Backward Pass
****

#### Basic Anatomy of Neural Network

![basic neural network](https://dl.dropboxusercontent.com/u/47591917/basic_neural_network.jpg)

above diagram show basic parts of nerual network, It contain 2 hidden layer (i.e. HL1, HL2) between input layer (X) and output layer (Y).

Lets go step by step from left to right and understand every part of it. 

#####1. Input (X):

given network we have two neuron in input layer. Xi in single input, x1 and x2 are part of input. They are column value of row of input matix X.

#####2. Hidden Layer (HL1/HL2):

hidden layer are layer between input and output layer.
Hidden layer help us to formulate more complex functions. HL1 and HL2 have 3 neuron unit each, every neuron unit represent particular feature.

#####3. Weight (W1/W2/W3):

Every neuron unit from one layer is connected to every neuron unit from next layer. These connection has some weight. This is parameter we change while learning. As we will see later in this post.

W1 is weight matrix of connection between input and hidden layer 1, Similary W2 and W3 are weight matrix of connection between HL1 to HL2 and HL2 to output(Y) respectively.


#####4. Bias (B1/B2/B3):

every hidden layer has bias. It is single column matrix. Usually help us to maintaining simplicity of network.
B1, B2 and B3 are bais of HL1, HL2 and output layer respectively.

#####5. Activation function (z):

activation function helps us to fire only neuron which really affected on output. It also help us to add non-linearity in neural network.
It is explained [here](https://github.com/chetandhembre/NN_Concepts/blob/master/basics/Activation%20Function.md#activation-function) in more details.

#####6. Output Layer(Y):

output layer has two neuron. It can represent different classes (classification problem) or real value (regression problem). So ouptut layer is output given by our activation function.

#####7. Loss function (L):

Loss function is last layer in neural network. As name suggest, this layer help us to find loss of neural network. Loss functions are explained in detail [here](https://github.com/chetandhembre/NN_Concepts/blob/master/basics/Loss%20Function%20and%20Cost%20Function.md#loss-function-and-cost-function)

These are basic parts of neural network. I have ommited some of part for sake of simplicity.

#### Forward Pass


When we try to predict output for given input, we do forward pass. It simply means we travel from left to right as shown in above diagram.

Lets go step by step in forward pass.

```
X - input to neural network.


h1 = X * W1 + B1    ---- Linear regression
h1 = z(h1)          ---- activation function

h2 = h1 * W2 + B2
h2 = z(h2)

h3 = h2 * W3 + B3
h3 = z(h3)

loss = L(h3, Y)
```
from above equation, we can represent `h3` using given all weights and biases as follow,

```
h3 = z(h3)
   = z(h2 * W3 + B3)
   = z(z(h1 * W2 + B2) * W3 + B3)
   = z(z(z(X * W1 + B1) * W2 + B2) * W3 + B3)
```


#### Backward Pass (Backpropagation):

From forward pass we figure out how neural network predict output. Idealy we want output of neural network equal to actual output(target).

We can measure `error` in calculating output by using [`cost function`](https://github.com/chetandhembre/NN_Concepts/blob/master/basics/Loss%20Function%20and%20Cost%20Function.md#loss-function-and-cost-function). Lets consider `C` is cost function.

We have to reduce `C` in order to increase accuracy of our neural network.

Cost function `C` is depend on output of network `h3`. So we can calculate any change in C with respect to h3 by `dC/dh3`. 
So any non zero value of `C` makes `dC/dh3` is non-zero, means `h3` contributed to error.

from calculation in forward pass we know how `h3` depends on weights, biases and input of model. So it is natural that weights and biases in mdoels contributes to error. (we are not considering input here as we can not change it).

`Backpropagation` algorithm uses [`chain rule`](https://github.com/chetandhembre/NN_Concepts/blob/master/utils/chain_rule.md#chain-rule) to calculate contribution of every weight and bias in final error.

![backpropagration](https://dl.dropboxusercontent.com/u/47591917/backpropagration_1.jpg)

above image show how backpropagation works.

```
        dC
dW3 = ----- = 𝛛3
       dh3

dW3 = reg_lambda * dW3 

B3 -= learning_rate * 𝛛3
W3 -= learning_rate * dW3
       
                dC        dC          dh3
dz2 = 𝛛z,2  = ------ =  ------- *  ---------   
                dz2       dh3         dz2

              dC          dC         dz2
dW2 = 𝛛2 =  -------  =  ------- *  -------     ---------(1) 
              dW2         dz2        dW2

              
dW2 = reg_lambda * dW2

B2 -= learning_rate * 𝛛2
W2 -= learning_rate * dW2

                dC        dC          dW2
dz1 = 𝛛z,1  = ------ =  ------- *  ---------     from eq. (1)
                dz1       dW2         dz1

              dC          dC         dz1
dW1 = 𝛛1 =  -------  =  ------- *  -------   
              dW1         dz1        dW1

              
dW1 = reg_lambda * dW1

B1 -= learning_rate * 𝛛1
W1 -= learning_rate * dW1   

```

above process exaplain how backpropagation works.

Backpropagtion is efficient algorithm to train model by only manipulating part of model which contributed in error.

We keep performing forward and backword pass till we reach point where cost function is minimum.

#### Example

Lets consider simple XOR solver in neural network.
this is how XOR gate behave, 

| X1 | X2 | Y |
|----|:--:|--:|
|  0 |  0 | 1 |
|  0 |  1 | 0 |
|  1 |  0 | 0 |
|  1 |  1 | 1 |

In order to solve it we are using following neural network.
![simple neural network](https://dl.dropboxusercontent.com/u/47591917/xor_neural%20network.jpg)

Lets explain neural network
```
Number of Neuron unit per layer

Input Layer[X] - 2
Hidden Layer[H] - 3
Activation Function - Sigmoid
Ouput Layer[Y] - 1
Cost Function - Softmax

Matrix Size

X - [2, 1]
W1 - [2, 3]
B1 - [3, 1]
W2 - [3, 2]
B2 - [2, 1]
Y - [2, 1]

Loss Function - Hinge Loss
Activation Function - Sigmoid
Optimizer - SGD
```


Let's consider some real values in order to get some intuition of nertwork.

```

     | 0  0 |       | 0 |
     | 0  1 |       | 1 |  
X =  | 1  0 |   Y = | 1 |
     | 1  1 |       | 0 | 

     |  0.91  0.22  -1.09 |        | -1.11 |
W1 = |                    |   b1 = | -0.57 |
     |  2.52  0.01   0.75 |        |  0.26 |
     
     | -1.19  -1.14 |         | -1.17 |
w2 = | -0.87  -0.08 |    b2 = |       |
     | -1.15  -0.94 |         | -2.05 |


```

We are using [`Stochastic Gradient Descent`](https://github.com/chetandhembre/NN_Concepts/blob/master/basics/optimizer.md#2-stochastic-gradient-descent-sgd), so lets initialize variables for it

```
learning_rate = 0.01
```

we are using [`Sigmoid`](https://github.com/chetandhembre/NN_Concepts/blob/master/basics/Activation%20Function.md#sigmoid) as our activation function.

[`Softmax loss`]() as loss function.

***Do not bother with lots of matric calculation below, My Intention is just show how we can do forward and backward pass by hand so we can easily replicate on computer***

***Do read comment between steps, It explains why we are doing in particular way, and what are problem with our model. Especially VANISHING GRADIENT issue***

In order to make thing simple, lets take one input (1, 1) with output (0) from sample, and apply forward and backward pass.
`X = [[1], [1]]` and `Y = [[1]]`
#### Forward Pass
![simple forward pass example](https://dl.dropboxusercontent.com/u/47591917/xor_forward_pass.jpg)

above image will make more clear about forward pass


```
w1.shape  = (2, 3)
x.shape = (2, 1)
h1.shape = (3, 1)


h1 = np.transpose(w1).dot(x) + b1                           - 1

h1 = |  0.91  2.52 |     | 1.0 |     | -1.11 |
     |  0.22  0.01 |  *  |     |  +  | -0.57 |
     | -1.09  0.75 |     | 1.0 |     |  0.26 |
     
   = |  2.32 |
     | -0.34 |
     | -0.08 |
     

sig_h1 = sigmoid(h1)                                     - 2
       = 1 / (1 + e ^ (-h1))             - element wise operation
       = | 0.91 |
         | 0.41 |
         | 0.48 |
         

h2 = np.transpose(w2).dot(sig_h1) + b2                      - 3

   = | -1.19 -0.87 -1.15 |   | 0.91 |   | -1.17 |
     |                   | * | 0.41 | + |       |
     | -1.14 -0.08 -0.94 |   | 0.48 |   | -2.05 |
     
  =  | - 3.16 |
     | - 3.57 | 

# softmax covert output to probability of getting given output
soft_h2 = softmax(h2)                                    
        = | 0.60 |
          | 0.40 |
so 1st and 2nd row give probability of getting XOR output for given input as '0' or '1' respectively

But for (1, 1) input we know XOR gives '0' as ouput.
Which means getting '0' has 1 probability while getting '1' havs 0 probability

we are calculating log likely hood loss.

loss = -np.sum(np.log(soft_h2[output]))
     = 0.51

we have to minimize loss.
 
gradient = soft_h2[output] - 1
         = | -0.4 |
           |  0.4 |
                  
```         

#### Backward Pass

lets see how backward pass works.
![simple backpropagation pass](https://dl.dropboxusercontent.com/u/47591917/xor_backpropagation.jpg)

this is simple representation of backpropagation.



```
gradient = | -0.4 |
           |  0.4 |



gradient of w1, b1, w2, b2, h1, sig_h1, will denoted by dw1, db1, dw2, db2, dh1, dsig_h1.
lets calculate each term using backpropagation alogorithm

gradient of term represent how much term have contributed to loss

from eq. 3, we can say that

dw2 = sig_h1.dot(np.transpose(gradient))

    = | 0.91 |   
      | 0.41 | * | -0.4 0.4 |
      | 0.48 |   
    
    = | -0.36  0.36 |
      | -0.16  0.16 |
      | -0.19  0.19 |
 
b2 gradient will be value of current gradient

db2 is same as gradient

db2 = gradient = | -0.4 |
                 |  0.4 |     


from eq 3, we can calculate, 

dsig_h1 = W2.dot(gradient)
        = | -1.19  -1.14 |    | -0.4 |
          | -0.87  -0.08 | *  |      |
          | -1.15  -0.94 |    |  0.4 |
        
        = | 0.02 |
          | 0.32 |
          | 0.08 |


from eq 2, we can calculate 

dh1 = sigmoid_backprop(h1, dsig_h1)
    = dsig_h1 * (sigmoid(h1) * (1 - sigmoid(h1))
    
    = | 0.02 |     | 0.91 |   | 0.08 |
      | 0.32 | * ( | 0.41 | * | 0.59 | )
      | 0.08 |     | 0.48 |   | 0.52 |
    
    = | 0.001 |
      | 0.077 |
      | 0.019 |

we can see here that dh1 is nearlly equal to 0.. this is mean sigmoid vanishing gradients.
This is one of the main problem with use of sigmoid

from equation 1, we can calculate 

dw1 = x.dot(np.transpose(dh1))

    = | 1 |     
      |   |  *  | 0.001 0.077 0.019 |
      | 1 |   
    
    =  | 0.001 0.077 0.019  |
       | 0.001 0.077 0.019  |

db1 is same as dh1 

db1 = | 0.01  |
      | 0.077 |
      | 0.019 |


we are using SGD as optimizer, so we can update w1, w2, b1 and b2 depend on their respective gradient.

w2 = w2 - learning_rate * dw2
    = | -1.19  -1.14 |          | -0.36  0.36 |
      | -0.87  -0.08 |  -  0.01 | -0.16  0.16 |
      | -1.15  -0.94 |          | -0.19  0.19 |
      
    = | -1.19 + 0.0036  -1.14 - 0.0036 |
      | -0.87 + 0.0016  -0.08 - 0.0016 |
      | -1.15 + 0.0019  -0.94 - 0.0019 |
    
    = | -1.186  -1.143 |
      | -0.868  -0.081 |
      | -1.148  -0.942 |

if we look at updated version of w2, we can see pattern first column correspond to 1st neuron
of output layer (i.e. output '0' with probability 1) is increased and second column value
decreases correspond to 2nd neuron of output layer (i.e. output '1' with probability 1).
This happpned because model want to increase probability of '0' as it just saw correct output as '0', This is learning of model.

b2 = b2 - learning_rate * db2
   = | -1.17 |          | -0.4 |
     |       | - 0.01 * |      |
     | -2.05 |          |  0.4 |
  
   = | -1.17 + 0.004 |
     | -2.05 - 0.004 |
   
   = | -1.166 |
     | -2.504 |

here also we can see pattern baise corresponding to 1st neuron is increased and
corresponding to 2nd neuron decreases because network was 0 as output recently.
 

w1 = w1 - learning_rate * dw1
   = |  0.91  0.22  -1.09 |           | 0.001 0.077 0.019  |
     |                    | - 0.01 *  |                    |
     |  2.52  0.01   0.75 |           | 0.001 0.077 0.019  |
     
   = | 0.91 - 0.00001  0.22 - 0.00077  -1.09 - 0.00019 |
     | 2.52 - 0.00001  0.01 - 0.00077   0.75 - 0.00019 |
   
   = | 0.90999  0.21923  -1.09019 |
     | 2.51999  0.00923   0.74981 |

w1 changes with very small amount after upating with gradient.
This happened because of vanishing gradient problem due to sigmoid activation function.

b1 = b1 - learning_rate * db1
   = | -1.11 |            | 0.01  |
     | -0.57 |  - 0.01 *  | 0.077 |
     |  0.26 |            | 0.019 |
   
   = | -1.11 - 0.0001  |
     | -0.57 - 0.00077 |
     |  0.26 - 0.00019 |
    
   = | -1.1101  |
     | -0.57077 |
     | 0.25981  |

we can see same pattern in b1 as w1.. b1 changes very little because of vanishing gradient problem.

Vanishing gradient cause not to backprop gradient in deep network.
```

I mentioned one single forward and backword pass. In order to increase accuracy of model we have to run this sequence for many interation so that `loss` will be less.

Here is [code](https://github.com/chetandhembre/NN_Concepts/blob/master/code/xor.py]) for above solution. 






