###Regularization
***

Regularization is very important part of neural network.

Regularization helps you to avoid [`overfitting`](https://github.com/chetandhembre/NN_Concepts/blob/master/utils/Overfiting%20and%20Underfiting.md#overfitting) problem.

Basic idea regularizor is to avoid blowing up weight of neural network or completely eliminate it.

#### Types of Regularization


##### 1. L2 Regularization

###### Formula
```
regulation_loss = 0.5 * lambda * sum(pow(Wi, 2))

where, 
lambda - hyperparameter, regularization parameter
0.5 use for convenient while gradient calculation
```
we add `regulation_loss` in total loss at output layer.


- [important of lambda](https://github.com/chetandhembre/NN_Concepts/blob/master/utils/ridge%20regression.md#effect-of-lambda-value) is explained here.
- uses [`ridge regression`](https://github.com/chetandhembre/NN_Concepts/blob/master/utils/ridge%20regression.md#ridge-regression)

###### Gradient
```
d(regulation_loss) = 2 * lambda * W
```

- we apply gradient at every layer in backpropagtion. Which is why we called L2 regularization is `Weight decay` feature
- L2 regularization do not eliminate features while predicting. It just make their importance (co-efficient) so small to demise it's role.


##### 2. L1 Regularization

###### Formula
```
regularization_loss = lambda * W

where,
Lambda - hyperparameter, regularization parameter
```
- [important of lambda](https://github.com/chetandhembre/NN_Concepts/blob/master/utils/ridge%20regression.md#effect-of-lambda-value) is explained here.
- uses [`lasso regression`](https://github.com/chetandhembre/NN_Concepts/blob/master/utils/Lasso%20Regression.md#lasso-regression)


###### Gradient
```
L1 regularization formula is not differentiable .. There are special ways to handle it

#TODO

```

- `sparsity` is very important feature of `L1` regularization, because L1 regularization can make some  of neural unit zero. So that gradient wont pass through them making them useless.
- sparsity leads to another feature know as `feature selection`.

***if you are not concerned with explicit feature selection, L2 regularization can be expected to give superior performance over L1***


#####3. Maxnorm

- Another form of regularization is to enforce an absolute upper bound on the magnitude of the weight vector for every neuron and use projected gradient descent to enforce the constraint.
- In practice, this corresponds to performing the parameter update as normal, and then enforcing the constraint by clamping the weight vector w⃗ w→ of every neuron to satisfy `‖w⃗ ‖<c`. 
- Typical values of c are on orders of 3 or 4. 
- Some people report improvements when using this form of regularization. 
- One of its appealing properties is that network cannot “explode” even when the learning rates are set too high because the updates are always bounded. 

####4. Dropout

Dropout is one of the most famous and important regularization technique, explained [here](https://github.com/chetandhembre/NN_Concepts/blob/master/papers/dropout.md)

Basic idea here is we drop some set of neuron while frontpropagation.

#####Inverted Dropout
- The undesirable property of the scheme presented above is that we must scale the activations by p at test time.
- Since test-time performance is so critical, it is always preferable to use inverted dropout.
- Which performs the scaling at train time, leaving the forward pass at test time untouched.
- Additionally, this has the appealing property that the prediction code can remain untouched when you decide to tweak where you apply dropout, or if at all

***

####Bias regularization
- It is not common to regularize the bias parameters because they do not interact with the data through multiplicative interactions, and therefore do not have the interpretation of controlling the influence of a data dimension on the final objective.
- However, in practical applications (and with proper data preprocessing) regularizing the bias rarely leads to significantly worse performance. 
- This is likely because there are very few bias terms compared to all the weights, so the classifier can “afford to” use the biases if it needs them to obtain a better data loss.


#### Per-layer regularization
- It is not very common to regularize different layers to different amounts (except perhaps the output layer).


#### What to use when?
- cross-validated L2 regularization works most of time
- we also apply dropout after every layer, 0.5 value of dropout parameter is reasonable most of time.
- Turn off dropout when you are evaluating on the validation/test set or if you want to compute error on the training set. Dropout was designed with the express intent of reducing overfitting, so if you are evaluating training loss with dropout turned on, you may see a higher training error.


#### Reference
- [cs231n](http://cs231n.github.io/neural-networks-2/#reg)