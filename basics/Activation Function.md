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

##### Derivative 
```
σ'(z) = 1
```


#### Step Function

following equaction says it all

```
              - 0 if z < 0 
             / 
h1 = σ(z) = -
             \_ 1 if z >= 0  
```

![step functiokn](http://i.stack.imgur.com/vRdzT.png)

##### Derivative 
```

         /- 0 for x != 0
σ'(z) = -
         \_ undefined for x = 0

```


#### Sigmoid

```
h1 = σ(z) = 1 / (1 + e ^ (-z))
```

![Sigmoid1]
(http://cs231n.github.io/assets/nn1/sigmoid.jpeg)

##### Derivative 
```
σ'(z) = σ(z)(1 - σ(z))
```


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

##### Derivative 

```
σ'(z) = (1 - σ(z)^2)
```

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

##### Derivative 

```

         /- 0 if z < 0
σ'(z) = -
         \- z if z >= 0

```

1. It greatly accelerate the convergence of SGD compare to sigmoid/tanh
2. Relu can be implemented by simply thresholding a matrix of activation at zero compare to more expensive operation of sigmoid/tanh


Relu units are fragile during training and can 'die' which mean gradient wont flow from these neuron making neural network wont learn feature represented by particular neuron

Sometime about 40% neuron die due to some wrong weight initializations

So be careful!!

#### Leaky Relu
```  
              _ az for z < 0
             /
h1 = σ(z) = -
             \_ z for z > 0
             
        
where a is small constant (0.01)
```
![Leaky Relu](http://lamda.nju.edu.cn/weixs/project/CNNTricks/imgs/leaky.png)


##### Derivative 

```

         /- a if z < 0
σ'(z) = -
         \- z if z >= 0

```

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

**Desire property of activation function** ([source](https://en.wikipedia.org/wiki/Activation_function))

#####1. Nonlinear: 

nonlinearity help you model more complex problem. with only two layer of nonlinear activation function we can have universal approximator. [Identiy function](https://github.com/chetandhembre/NN_Concepts/blob/master/basics/Activation%20Function.md#identity-function) is linear function. so even we created multiple layer NN with identity function as activation function it will be same as single layer model

#####2. Continuously differentiable:
during gradient base backprop we take derivative of output of activation function to pass gradient. So non contunous function do not have derivatives. The [binary step activation function](https://github.com/chetandhembre/NN_Concepts/blob/master/basics/Activation%20Function.md#step-function) is not differentiable at 0, and it differentiates to 0 for all other values, so gradient-based methods can make no progress with it.

#####3. Range:
When the range of the activation function is finite, gradient-based training methods tend to be more stable, because pattern presentations significantly affect only limited weights. When the range is infinite, training is generally more efficient because pattern presentations significantly affect most of the weights. In the latter case, smaller learning rates are typically necessary.

#####4. Monotonic:
When the activation function is [monotonic](https://github.com/chetandhembre/NN_Concepts/blob/master/utils/monotonic%20function.md), the error surface associated with a single-layer model is guaranteed to be convex.

#####5. Smooth:
Functions with a Monotonic derivative have been shown to generalize better in some cases. The argument for these properties suggests that such activation functions are more consistent with Occam's razor
(do not understand what it means)

#####6. Approximates identity near the origin:
When activation functions have this property, the neural network will learn efficiently when its weights are initialized with small random values. When the activation function does not approximate identity near the origin, special care must be used when initializing the weights.Activation functions where `f(0)=0` and `f'(0)=1` and `f'` is continuous at 0.



| Name        | Non Linear | Continuously differentiable |  range | Monotonic | Approximates identity near the origin |
|:------:	    | :---------:| :--------------------------:| :-----:| :--------:| :-----------------------------------: |
|[Identity Function](https://github.com/chetandhembre/NN_Concepts/blob/master/basics/Activation%20Function.md#identity-function)| :x: | :heavy_check_mark:| ( -∞, +∞ ) |  :heavy_check_mark: | :heavy_check_mark:|
|[Step Function](https://github.com/chetandhembre/NN_Concepts/blob/master/basics/Activation%20Function.md#step-function)| :heavy_check_mark:| :x: | ( 0, 1 ) |  :heavy_check_mark: | :x:|
|[Sigmoid](https://github.com/chetandhembre/NN_Concepts/blob/master/basics/Activation%20Function.md#sigmoid)| :heavy_check_mark:| :heavy_check_mark: | ( 0, 1 ) |  :heavy_check_mark: | :x:|
|[Tanh](https://github.com/chetandhembre/NN_Concepts/blob/master/basics/Activation%20Function.md#tanh)| :heavy_check_mark:| :heavy_check_mark: | ( -1, 1 ) |  :heavy_check_mark: | : heavy_check_mark:|
|[Relu](https://github.com/chetandhembre/NN_Concepts/blob/master/basics/Activation%20Function.md#relu)| :heavy_check_mark:| :heavy_check_mark: | [ 0,  ∞) |  :heavy_check_mark: | :x:|
|[Leaky Relu](https://github.com/chetandhembre/NN_Concepts/blob/master/basics/Activation%20Function.md#leaky-relu)| :heavy_check_mark:| :heavy_check_mark: | ( -∞,  ∞) |  :heavy_check_mark: | :x:|
|[Maxout](https://github.com/chetandhembre/NN_Concepts/blob/master/basics/Activation%20Function.md#maxout)| :no_mouth:  | :no_mouth: | :no_mouth: |  :no_mouth: | :no_mouth: |
|[Softmax](https://github.com/chetandhembre/NN_Concepts/blob/master/basics/Activation%20Function.md#softmax)| :no_mouth:  | :no_mouth: | :no_mouth: |  :no_mouth: | :no_mouth: |
