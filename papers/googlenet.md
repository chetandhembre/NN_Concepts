# GoogleNet (original)

paper [link](http://arxiv.org/pdf/1409.4842v1.pdf)

#### Significance

- won imagenet challange 2014

#####  Motivation

increasing depth of network/ size of training data are good way to create good model to solve image classification problem

- cons of this approach
  -  prone to overfitting
  -  creating high quality training data is tricky
  -  increase in size (depth and width) of network dramatically increase computation resource.

##### Architecture Details (Inception architecture)

> The main idea of the Inception architecture is based on finding out how an optimal local sparse structure in a convolutional vision network can be approximated and covered by readily available dense components

if you consider translational invariance it means we can store/represent all information (dense matrix) with very small data(sparse matrix). this is motto behind this paper

lets see how they achieve it

##### Inception module (naive version)
![inception module naive version](https://raw.githubusercontent.com/stdcoutzyx/Blogs/master/papers/imgs/5-1.png)


you can see there five main blocks

1. 1x1 convolution filters layers
2. 3x3 convolution filters layers
3. 5x5 convolution filters layers
4. 3x3 max pool layer
5. filter concatenation layers

1x1, 3x3 and 5x5 convolution layers can/will reduce depth(k) of input and max pool layer will reduce spatial (height and width) dimensions of input.

######why use different filtering layer simultaneously?

after looking at image we can say why we have to use different size of convolution filters simultaneously. 

we need to consider two points
1. inception module depends on `translational invariance` which means object's position wont affect meaning of object.
2. convolution filter with different size can cover different cluster of information. 

we due to point two we have different size of filters (1x1, 3x3 and 5x5) but these filter size are selected depend on convenience.

> current incarnations of the Inception architecture are restricted to filter 1x1,3x3 and 5x5 sizes, however this decision was based more on convenience rather than necessity.

and selection of pooling layer may be due to fact that in other layer it worked

and what about filter concatenation layer?

![filter concatation](https://dl.dropboxusercontent.com/u/47591917/googlenet_stackup.png)


##### cons of this approach
>One big problem with the above modules, at least in this naive form, is that even a modest number of 5x 5 convolutions can be prohibitively expensive on top of a convolutional layer with a large number of filters.  This problem becomes even more pronounced once pooling units are added to the mix:their number of output filters equals to the number of filters in the previous stage.  The merging of the output of the pooling layer with the outputs of convolutional layers would lead to an inevitable increase in the number of outputs from stage to stage. Even while this architecture might cover the optimal sparse structure, it would do it very inefficiently, leading to a computational blow up with in a few stages.

what it says?
1. as we are using 5x5 conv layer with large number of filters then number of parameter will increase a lot.
2. and another problem is adding pooling layer o/p will increase dimension of output. as we know pooling wont change depth of network. so lets take example
```
we have three convolution filters i.e. (1x1, 3x3 and 5x5). lets say if we have i/p of size (28 x 28 x 192). we can choose value of `k` much smaller than 192. and we want spatial dimension for o/p same so stride will be always 1. so we will have output (28 x 28 x k). But we are adding pooling layer output which will be of size (28 x 28 x 192) to total size of o/p of conv network will be (28 x 28 x (192 +k)). 
```

#### Inception module with dimension reduction
![inception module with dimension reduction](https://hijeffery-prml.rhcloud.com/wp-content/uploads/2014/09/Inception-Module.png)

you can see extensive use of 1x1 conv layer. here main purpose of 1x1 filter is to `dimension reduction`.

1x1 convolution also add `relu` non linearity. 

>In general, an Inception network is a network consisting of modules of the above type stacked upon each other, with occasional max-pooling layers with stride 2 to halve the resolution of the grid. For technical reasons (memory efficiency during training), it seemed beneficial to start using Inception modules only at higher layers while keeping the lower layers in traditional convolutional fashion.This  is  not  strictly  necessary,  simply  reflecting  some  infrastructural  inefficiencies  in  our  current implementation.

##### Pros of Architecture

>One of the main beneficial aspects of this architecture is that it allows for increasing the number of units at each stage significantly without an uncontrolled blow-up in computational complexity. The ubiquitous use of dimension reduction allows for shielding the large number of input filters of the last stage to the next layer, first reducing their dimension before convolving over them with a large patch size.  Another practically useful aspect of this design is that it aligns with the intuition that visual information should be processed at various scales and then aggregated so that the next stage can abstract features from different scales simultaneously


#### Backpropagation
>Given the relatively large depth of the network, the ability to propagate gradients back through all the layers in an effective manner was a concern.  One interesting insight is that the strong performance of relatively shallower networks on this task suggests that the features produced by the layers in the middle of the network should be very discriminative.  By adding auxiliary classifiers connected to these intermediate layers, we would expect to encourage discrimination in the lower stages in the classifier, increase the gradient signal that gets propagated back, and provide additional regularization.  These classifiers take the form of smaller convolutional networks put on top of the output of the Inception (4a) and (4d) modules.  During training, their loss gets added to the total loss of the network with a discount weight (the losses of the auxiliary classifiers were weighted by 0.3).  A tinference time, these auxiliary networks are discarded.


#### final convolution neural network
![final network](http://homes.cs.washington.edu/~jmschr/lectures/googlenet.png)

[ethereon visualization](http://ethereon.github.io/netscope/#/preset/googlenet)
#### Resources
1. http://wikicoursenote.com/wiki/GoingDeeperWithConvolutions
2. http://iamaaditya.github.io/2016/03/one-by-one-convolution/
3. https://classroom.udacity.com/courses/ud730/lessons/6377263405/concepts/63713420390923#
4. https://www.reddit.com/r/MachineLearning/comments/2gp385/googlenet_slides_from_eccv_2014_workshop/






