###Lasso Regression

lasso regression help us to solve problem of `overfitting`.

Overfitting occures when you have very `High Variance Error`. explained [here](https://github.com/chetandhembre/NN_Concepts/blob/master/utils/bias%20variance%20tradeoff.md)

#### Prerequisites

- you should have two or more features

lasso regression use L1 [vector norm](https://github.com/chetandhembre/NN_Concepts/blob/master/utils/Vector%20Norm.md)

```
c = |x1| + |x2| + ... |xn|
```

basic idea is we do not want to keep our weight sum under `c`.


So const function becomes

```
L(Bo, B1, lambda) = min((Y - A * B)^2) + lambda * sum(|| B ||)
```

Lasso regression is of shape diamond. compare to ridge which is circle.

![lasso regression graph](https://www.applied-mathematics.net/identification/imgLARS/lasso.png)

from above graph it is clear that cost function touches at corner of diamond because of it we get some feature's value as zero.



####Features

- increases sparcity of model, which in return avoid overfitting.
- it helps you in feature selection.


#### Differene between Ridge and Lasso regression

- shape of lasso regression weight penalty is diamond, but ridge regression shape is circle
- lasso regression make co-efficient zero for some of features which is not possible in ridge regression
- lasso regression do not have simple formula to calculate like ridge regression. You can to use program to find out.


#### Reference
- [youtube](https://www.youtube.com/watch?v=5asL5Eq2x0A)