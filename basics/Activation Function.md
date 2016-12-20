###Activation Function
in multilayer neural network one layer output is feed as i/p to next layer, Layer o/p depends calculated by multiplying i/p and weight (sometime we also add bias). `activation function`  as name suggest decide how o/p from previous layer feed to next layer.
I mean we can can convert o/p of previous layer to binary value i.e. 0 and 1 i.e if o/p is below threshold then consider it as 0 otherwise 1. This is just one of the way we can interpret o/p of hidden layer with help of activation function

Activation function also helps to bring `non-linearity` which is very useful to solve complex problem with deep neural network.

```
h1 = σ(xw + b)

where
σ: activation function 
x: input 
w: weight
b: bias
h1: output
```

### Types of acivation function

#### Identity Function

as name suggest it output same value as input
```
h1 = σ(z) = z
```

![Identity Function](http://i.stack.imgur.com/NKESX.png)

#### Step Function

following equaction says it all

```
              - 0 if z < 0 
             / 
h1 = σ(z) = -
             \_ 1 if z > 0  
```

![step functiokn](http://i.stack.imgur.com/vRdzT.png)

#### Sigmoid

```
h1 = σ(z) = 1 / (1 + e ^ (-z))
```

![Sigmoid1]
(http://cs231n.github.io/assets/nn1/sigmoid.jpeg)

from above graph it is created that any output from previous layer will get squashes between 0 and 1.
It is nice progress from `step function` which define if neuron will fire or not. Sigmoid function gives little sense of non linearity. 

As you can see from graph it is clear that for large positive of o/p sigmoid will make them 1 and for  large negative value it will convert to 0 i.e. saturating those values as reducing effect of them

1. `Sigmoids saturates and kill gradients`. It is related to the way sigmoid squashes input between 0 and 1. So will backprop if gradient is very small then it will become 0 and wont flow which make neural network unlearnable
2. `Sigmoid output are not zero-centered`. we can see output of sigmoid is between 0 and 1 i.e. it will always be positive or negative which can create problems while backpropagation.

#### Tanh
```
h1 = σ(z) = tanh(z)
``` 
![Tanh](http://cs231n.github.io/assets/nn1/tanh.jpeg)

as graph suggest tanh squashes input between -1 and 1. It solves `non zero centered ouput` issue thats why we preferred `tanh` over `sigmoid`.
tanh is simply scaled sigmoid neuron
```
tanh(x) = 2σ(2x) - 1
```

#### Relu
```
h1 = σ(z) = max(0, z)
```
the activation simply threshold at zero

![Relu](http://cs231n.github.io/assets/nn1/relu.jpeg)

1. It greatly accelerate the convergence of SGD compare to sigmoid/tanh
2. Relu can be implemented by simply thresholding a matrix of activation at zero compare to more expensive operation of sigmoid/tanh


Relu units are fragile during training and can 'die' which mean gradient wont flow from these neuron making neural network wont learn feature represented by particular neuron

Sometime about 40% neuron die due to some wrong weight initializations

So be careful!!

#### Leaky Relu
```  
              _ az for x < 0
             /
h1 = σ(z) = -
             \_ x for x > 0
             
        
where a is small constant (0.01)
```
![Leaky Relu](http://lamda.nju.edu.cn/weixs/project/CNNTricks/imgs/leaky.png)

it just tring to avoid dying neuron problem by instead of making all negative o/p to zero but mapping to very small negative value

results are not consistent with this method


#### Maxout
```
h1 = max(transpose(w1)x + b1, transpose(w2)x + b2)
```

this is triky actiation function which does not follow normal `f(transpose(w)x + b)` format where f is activation function.

beauty of this activation function is 	`relu` and `leaky relu` are special case of it.

So say if we have w1 and b1 0 then we get relu.

`maxout` enjoy benefits for both relu and leaky relu so it wont have dying neuron issue.

But it will double the number of parameters for every single neruon.

more explaination is [here](https://github.com/chetandhembre/NN_Concepts/blob/master/papers/maxout.md)

####Softmax
softmax activation function try to squash every output of neuon between (0, 1] like many of other activation function do.

Sum of output of `softmax` function for all neuron `1`.

Which means it give probability of occurance of feature provided by particular neuron unit.

![softmax function fomula](https://jamesmccaffrey.files.wordpress.com/2016/03/softmaxequation.jpg)

![softmax-output-squashing](https://qph.ec.quoracdn.net/main-qimg-cc09d4e526c39dddfe957b280a2e4f0c?convert_to_webp=true)


**softmax activation function in output layer**

because
* as you can see it squashes output between (0, 1].  in hidden layer it may kill gradient
* output of neuron is dependent to each other.. it can lead to overfiting


**Advice from cs231n class about selecting activation function**
```
Use the ReLU non-linearity, be careful with your learning rates and possibly monitor the fraction of “dead” units in a network. If this concerns you, give Leaky ReLU or Maxout a try. Never use sigmoid. Try tanh, but expect it to work worse than ReLU/Maxout.
```




