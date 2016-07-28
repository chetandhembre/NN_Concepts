#ResNet

paper [link](http://arxiv.org/pdf/1512.03385v1.pdf)

###### Significance

- won ILSVRC 2015 classification challenge with big margin
- won ImageNet detection
- won Imagenet localization
- won COCO segmentation
- won COCO detection

###### does deep NN give better result than their shallow counterpart ?

experiments shows that deeper NN after certain depth start performing worst compare to their shallow counterpart

Problems

1. [vanishing/exploding gradients](https://www.quora.com/What-is-the-vanishing-gradient-problem): 

      this can be solved by use of batch normalization
2. degradation
   
     as we increase layer accuracy of network get saturated and it is not due to overfitting.

> The degradation (of training accuracy) indicates that not
all systems are similarly easy to optimize. Let us consider a
shallower architecture and its deeper counterpart that adds
more layers onto it. There exists a solution by construction
to the deeper model the added layers are identity mapping,
and the other layers are copied from the learned shallower
model. The existence of this constructed solution indicates
that a deeper model should produce no higher training error than its shallower counterpart. But experiments show that our current solvers on hand are unable to find solutions that are comparably good or better than the constructed solution (or unable to do so in feasible time)

`resnet` proposed solution to 2nd problem related to deep NN.

Proposed Solutions

- paper proposed deep NN with `deep residual learning framework` block.


###### What is residual learning block?

`residual learning block` is main thing this paper proposed to avoid `degradation` problem in deep NN.

![residual learning block](https://matrixmashing.files.wordpress.com/2016/01/residualunit.png?w=485&h=231)

 - every layer it optimized for residual mapping.
 - there will be shortcut connection which can skip one for more layers. And they perform `identity mapping` as image above suggests.
 - it does not add any extra hyper-parameter and do not increase computational complexity. We can use normal SGD and backprop.

apparently (I have not read paper yet) `highway network` also use `shortcut connection`. But difference is in highway network shortcut connections is gated (need to know what is means :D). It means shortcut connection cannot be used for certain time. But in ResNet shortcut connections are identity mapping not a gate so they always remain open.

>Concurrent with our work, “highway networks” [42, 43]
present shortcut connections with gating functions [15].
These gates are data-dependent and have parameters, in
contrast to our identity shortcuts that are parameter-free.
When a gated shortcut is “closed” (approaching zero), the
layers in highway networks represent non-residual functions.
On the contrary, our formulation always learns
residual functions; our identity shortcuts are never closed,
and all information is always passed through, with additional
residual functions to be learned. In addition, high-way networks have not demonstrated accuracy gains with
extremely increased depth (e.g., over 100 layers).

#####Deep Residual Learning

######1. Residual Learning


- we have original mapping `H(x)`
- residual function `f(x) = H(x) - x`
- so original function becomes `H(x) = f(x) + x`

if we can optimize for H(x) then we can easily optimized for `f(x) + x`. given that x has same dimension in i/p and o/p.

>In real cases, it is unlikely that identity mappings are optimal,
but our reformulation may help to precondition the problem. If the optimal function is closer to an identity
mapping than to a zero mapping, it should be easier for the
solver to find the perturbations with reference to an identity
mapping, than to learn the function as a new one. We show
by experiments (Fig. 7) that the learned residual functions in
general have small responses, suggesting that identity mappings provide reasonable preconditioning.

so this is what i learned after reading [this](https://deepmlblog.wordpress.com/2016/01/05/residual-networks-in-torch-mnist/)
```
Suppose you have a layer L, which takes as input x and gives output  y = L(x). If the layer has to learn a function y = 0, then L need not learn much and have all weights as zero. If the layer has to learn a function y = x, it has a much harder time to learn the identity function and have to learn its weights according. 
```
######Identity mapping by Shortcuts

residual learning block equation to optimize
```
y = F(x, {Wi}) + x
```

- x: i/p
- y: o/p
- F(x, {Wi}): residual mapping to be learned

for multiple layer we can have
```
F = W2σ(W1x) 
```

where `σ` is ReLU,

>The dimensions of x and F must be equal in Eqn.(1).
If this is not the case (e.g., when changing the input/output
channels), we can perform a linear projection Ws by the
shortcut connections to match the dimensions:
```
y = F(x, {Wi}) + Wsx.
```

F can have one or more layers.
F with single layer become linear classifier which will not have any advantage


######Network Architecture

- 3x3 conv filter
- downsampling directly by conv layer with 2 stride
- global average pooling layer
- 1000 way fully connected layer with softmax
- 34 weighted layer
- 224 x 224 image size
- per pixel mean subtracted
- batch normalization after every conv layer before activation layer
- SGD with 256 batch size
- The learning rate
starts from 0.1 and is divided by 10 when the error plateaus
- trained upto 60 × 10^4 iterations
- weight decay of 0.0001 and a momentum of 0.9
- did not used dropout


####Experiments
######ImageNet Classification

![resnetvsplain](https://dl.dropboxusercontent.com/u/47591917/NN_Concept/resnetvsplain.png)

- as number of layer increase plain NN performed worse
- but in resnet as number of layers increases it perform better
- uses resnet added shortcut connection after pair of 3x3 conv filters other architecture is same as plain NN.
- interestingly 18 layer plain NN and resnet perform same only resnet converge quickly at earlier stage. It means resnet only helpful when you large number of layers

######Identity Vs Projection shortcut

- identity shortcut perform very well with out increasing lot of complexity
- use projection shortcut only when you have to change o/p dimension compare to i/p dimension.

######Deeper Bottleneck Architectures
- in practice instead of using two 3x3 conv layer, they use 1x1 - 3x3 - 1x1 conv layer to decrease time for learning
- 1x1 conv layer use to reduce and restore dimensions in order make 3x3 conv layer efficient.
- projection
shortcuts are used for increasing dimensions, and other
shortcuts are identity

`*** what it mean by projection?`

so new architecture looks like

![new arch resnet](https://dl.dropboxusercontent.com/u/47591917/NN_Concept/resnet_newarch.png)

######Visualization



######blog
- http://torch.ch/blog/2016/02/04/resnets.html
- https://deepmlblog.wordpress.com/2016/01/05/residual-networks-in-torch-mnist/

######implementations

- by author of paper [link](https://github.com/KaimingHe/deep-residual-networks)
