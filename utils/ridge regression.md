###Ridge Regression

ridge regression help us to solve problem of `overfitting`.

Overfitting occures when you have very `High Variance Error`. explained [here](https://github.com/chetandhembre/NN_Concepts/blob/master/utils/bias%20variance%20tradeoff.md)

#### Prerequisites

- you should have two or more features

ridge regression use L2 [vector norm](https://github.com/chetandhembre/NN_Concepts/blob/master/utils/Vector%20Norm.md)

```
c = pow(sum(pow(Xi, 2)), 2)
```

Basic idea is to avoid exploiding weights i.e. (x1, x2, .. , xn). If we allowed them to grow without constrain it will overfit to given sample training data.

So in ridge regression we try to 

```
min ||y - AX||^2 such that ||X||^2 <= c2
```

what it meas is we want to reduce error while predicting output for given training data such that L2 norm of features (x1, x2, .. xn) can be more than certrain c^2 value. 

![geometrical representation of ridge regression](http://rasbt.github.io/mlxtend/user_guide/general_concepts/regularization-linear_files/l2.png)

from above plot it is clear that we will add penalty to error so that weight will remain within L2 norms.

lets represent it in calculus

consider
 
```
let represent 
min(sum( pow( y - Bo - B1x1 - ...), 2)) as  E(Bo, B1, ... Bn)

so loss in ridge regression will be

L(Bo, B1, .. Bn) = E(Bo, B1, .., Bn) + lambda * (|| B ||^2 - c^2)

where,
L - loss function
lambda - hyper parameter to adjust penalty
```

from above equation it is clear that if `B` increase then loss function penalty will be high to make sure `B` remains in constrain.

#### Ridge Solution
```
ridged(B) = inverse((trans(X) * X + lambda * I)) * trans(X) * Y

where,
I - identity matrix
```

***ridge regression wont make B zero, it means we will not eliminate any feature from model while predicting. It just reduce influence of them to very small value***

***ridge regression introduce bias in model***


#### Effect of Lambda Value

#####1. lambda is Big: 
It will lead to `underfitting`.
then we are having large penalty in loss and might reduce influence of features in predicting model.

#####2. lambda is Small
It will lead to `overfitting`
small lambda means less penalty so weight of some feature might grow large to increase influence in prediction of model


#### Where to use?
1. when you have larger number of variables with correlation.
#ToDO




#### Reference 
1. [youtube](https://www.youtube.com/watch?v=5asL5Eq2x0A&index=5&list=PLvcbYUQ5t0UFhdkiCojiFOygmbMU19BFq)