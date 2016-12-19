##Dropout

Paper [link](https://www.cs.toronto.edu/~hinton/absps/JMLRdropout.pdf)
####Autors
* Nitish Srivastava
* Geoffrey Hinton 
* Alex Krizhevsky
* Ilya Sutskever
* Ruslan Salakhutdinov

#### Problem trying to solve
1. overfiting of network
2. regularizor

#### Overfiting

as we need to more deep network (more number of hidden layer) to extract complext features from data, we need very large amount of data.. but may not possible to get every time. Which lead to train deep network on small train data. Problem with this approach is overfiting.

##### What is overfiting?
Usually every unit in NN represent some features of data. If we train NN on small data for large number of epoch. Many such unit co-operate which each other to represent features relation which may not present in actual data.

Overfiting causes to give very good train time accuracy but at test time it's accuracy drops dramatically as it sees new data and NN do not understand relations.

##### Solution to Overfiting?
1. stop training when performance on validation set start getting worse.. 
2. use L1 or L2 regularizor
3. use soft weight

There is another solution for this called [bagging](https://github.com/chetandhembre/NN_Concepts/blob/master/utils/Bootstrap%20Aggregation(bagging).md). in gist what it means is to create many different model and train on smaple from given small training data and finally average the results.

Problems with bagging are
1. need to train large number of NN
2. tunning hyperparameters for these NN can be very time consuming task


```
dropout essentially "bagging" done effeciently
```

#### Basic Idea
dropout is basically base on two important trics.
1. drop units from NN layer with probability `p`. which mean every time we drop new unit from layer we are creating new NN and all these NN shares same weights
2. `model averaging`.. in bagging we usually take average of many NN's output. But as number of different model in dropout are so large it will be very difficult to do it. So dropout solve problem by taking [`geometric mean`](https://github.com/chetandhembre/NN_Concepts/blob/master/utils/geometric%20mean.md).

![dropout](http://cs231n.github.io/assets/nn2/dropout.jpeg)
#### How does Dropout work?
1. Training Time
	* we drop unit from every layer with probability `1 - p`
2. Test Time
   * if any unit retain with probability `p` then we multiply weigth of neuron by `p`

![training-testing-dropout](http://files.hapd.info/pics/uploads/paper/dropout2.png)


#### Model Description
* Feed Forward Pass

```

rj(l) = Bernoulli(p)

y(l) = r(l) * y(l)

zi(l) = wi(l+1) * y(l) + bi(l+1)

yi(l+1) = f(zi(l))

where f is activation function
```

* Backpropagtion

same as standard NN. only pass gradient changes from unit which actually took part in creating gradient for given dropout probability `p`

#### Features of Dropout

* we are droping neuron unit with probability `1 - p`. It makes sure that no two neuron come togethor to respresent feature from data. thus avoids overfiting. 
* Every neuron learn something on it's own.



#### Implementation Observation
* work better when learning rate it high as dropout adds noise in data
* it should be 10-100 time more than SGD
* momentum value should be 0.95 to 0.99 compare to 0.9 for standard NN
* work better with `maxout` activation function.
* hidden layer optimal dropout probability is `0.5`
* input layer optimal probability is 0.8-1
* does not go well with `data agumentation`