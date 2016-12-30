### Bias Variance Tradeoff

This is classical problem face in regression as well as classification problem. 
Lets get started.

#### Bias
Bias happen when our prediction model only consider part of parameter(features) to predict output. It means model is bias toward some set of features from data. `Underfitting` of model happens because of bias

#### Variance
Variance defined as "how spread data points are from mean value of give sample data."
Overfitting of model is related to variance of distribution.

#### Bias Error
```
amount by which the expected value from model differes from true value or target function.
```

- Bias error is related to `simplicity` of model
- Higher the bias error simpler the model
- Higher Bias Error model tend to underfit. 


##### Formula
```
Bias[f'(x)] = E[f'(x) - f(x)]

where,
f'(x) is prediction model
f(x) is true model
```

#### Variance Error
```
Amount by which prediction, over one training set difference from true value over multiple sample of training data
```

- Variance error define how inconsistent prediction from one another
- High variance error lead to overfitting of data
- model become mode complex

##### Formula
```
Var[f'(x)] = E[f'(x)^2] - E[f'(x)]^2

where,
f'(x) - prediction model
```

### Square Error
overall we try to create model which will give least square error during test time.
square error consists of two part
1. reducable error
2. irreducable error


```
E[(y - f'(x))^2] = Bias_E[f'(x)]^2  + Var[f'(x)] + e
```

Bias error and variance error are reducable error and `e` is irreducable error

### Relation between bias error and variance error

- Lower bias error gives as more complex model but it can increase variance, because it try to accomodate all features while predicting, it overfit model
- Higher bias error leads to more simpler model which will have less variance but it can undefit model

Here is simple diagram which explain relation between bias error and variance error

![bais_variance_tradeoff](https://dl.dropboxusercontent.com/u/47591917/bias_variance_tradeoff.png)


Here how bias and variance changes as we increase complexity of model

![relation between complexity of model and bias/variance](http://insidebigdata.com/wp-content/uploads/2014/10/Bia_variance_tradeoff_fig.jpg)
#### Bias and Variance Tradeoff

Ideal model should able to capture all regularity between feature of data and it should generalized enough to handle unseen data. If you want to capture all regularity among features then we have to have complex model(high variance) and to create generalized model we have to have simpler model (high bias).

This is tradeoff we have to do while creating model.

#### How to handle tradeoff?

1. regularization is used to handle high variance
2. model we can decrease bias by increasing number of hidden layers.
3. k-nearest neighbor models, a high value of k leads to high bias and low variance
4. decision trees, the depth of the tree determines the variance. Decision trees are commonly pruned to control variance.

One way of resolving the trade-off is to use mixture models and ensemble learning.For example, boosting combines many "weak" (high bias) models in an ensemble that has lower bias than the individual models, while bagging combines "strong" learners in a way that reduces their variance.

#### Reference

1. [wikipedia](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff)
2. [blog](http://insidebigdata.com/2014/10/22/ask-data-scientist-bias-vs-variance-tradeoff/)
3. [blog](http://scott.fortmann-roe.com/docs/BiasVariance.html)




