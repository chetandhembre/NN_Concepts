###[Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification](http://www.cv-foundation.org/openaccess/content_iccv_2015/papers/He_Delving_Deep_into_ICCV_2015_paper.pdf)

This paper is important because this is first paper which gives us better than human level performanc in [ILSVRC](http://www.image-net.org/challenges/LSVRC/) task.

```
we achieve 4.94% top-5 test error on the ImageNet 2012 classification dataset.
This is a 26% relative improvement over the ILSVRC 2014 winner (GoogLeNet, 6.66% [33]).
To our knowledge, our result is the first1
to surpass the reported human-level performance (5.1%, [26]) on this dataset.

```

Paper is divided into Three Parts

1. Introduction to PRELU
2. Theoritical initialization for PRELU
3. Architecture of network

###1. PReLu
It is advanced version of [ReLu](https://github.com/chetandhembre/NN_Concepts/blob/master/basics/Activation%20Function.md#relu).

We know ReLU Activation function defined as follow

```

         /- 0 if z < 0
σ'(z) = -
         \- z if z >= 0

```

from above formula we can conclude following things
1. It is non symetric function. (Sigmoid and tanh are sysmetric function)
2. average response of Relu will be never negative.

Second point can be tricky because we are effectively converting negative values to zero which leads for dieing of connection.

Paper Propose varient of Relu called `PRelu (Programmable Relu)`

![Relu And Prelu](https://dl.dropboxusercontent.com/u/47591917/relu%20and%20prelu.png)


Equation of PRelu can be given as following

```

         /- zi   if z > 0
σ(zi) = -
         \- aizi if z <= 0

```

- ai controling steep in negative part of relu.
- i represent different channel in individual layer l.

We can have shared a coefficient in single layer.

Paper mentioned that `PReLu` gives better performance than Relu with out increasing number of parameters.

#### Special Cases
- when a = 0 then PRelu becomes Relu
- when a is not learnable then it become [Leaky Relu](https://github.com/chetandhembre/NN_Concepts/blob/master/basics/Activation%20Function.md#leaky-relu), usually initialized with 0.01

Leaky Relu avoid zero gradient problem but it do not increase accuracy significantly.

We have to note that a co-efficient is learnable parameter. Paper suggest to use `momentum` method to update `a`

```

Δai = u * ai + 𝞊 * (dE / dai)

u -  momentum parameter
𝞊 - learning rate 
(dE / dai) -  gradient from next layer with respect to ai
```

They initialize `a` to `0.25`

Important thing paper mentioned is they did not use weight decay (L2 regularization).

```
It is worth noticing that we do not use weight decay (l2 regularization) when updating ai.
A weight decay tends to push ai to zero, and thus biases PReLU toward ReLU.
Even without regularization, the learned coefficients rarely have a magnitude
larger than 1 in our experiments.
```

#### BackPropagation
```

         /- aizi   if z <= 0
σ'(zi) = -
         \- zi if z > 0

```

#### Gradient with respect to a (dE / dai)
```
                 - 0  if zi > 0 
   df(zi)      / 
---------- = -
   dai         \_  zi  if zi <=0
```


###2. Theoritical initialization for PRELU

Paper also suggest some initialization for Relu in order to get most out of PRELU.

But it is theoritical, It is not practically proven.

In simple term.
Initialize `W` such that.

1. Mean is zero
2. Variance is, 
  
   ```
	Var[Wl] = 2 / nl
	
	Var[Wl] - variance of weight initialization at layer l
	nl - number of neuron at layer l
	```
3. `bl = 0`

This zero mean gaussian distribution has standard deviation `np.sqrt(2 / nl)`.

###3. Architecture of network

TODO