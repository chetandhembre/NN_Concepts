### BootStrap Aggregation (Bagging)

#### Usefulness
* `bagging` is use for creating predictive model for data with high variance
* improve performance of unstable algorithm like nerual network, decision tree.
* a learning algorithm is informally called un stable if small changes in the training data lead to significantly different models and relatively large changes in accuracy. Unstable learner has low bias but high variance.



#### Process

lets say we have sample of training data which has high variance. So we will create lot of sample data with replacement and train (more of overfit) out predictive model on it.
When we try to predict answer on our training data,  we just aggregate output of every predicitve model and select best one.

Consider a dataset Dn and a learning procedure to build an hypothesis αn from Dn. The idea of bagging or bootstrap aggregating is to imitate the stochastic process underlying the realization of Dn. A set of B repeated bootstrap samples D(b)n, b=1,…,B are taken from Dn. A model α(b)n is built for each D(b)n. A final predictor is built by aggregating the B models α(b)n. In the regression case the bagging predictor is

```

hbag(x) = 1 / b * (sum [b =1 to B] h(x, a(b)n))
```

#### Reference
1. http://stats.stackexchange.com/questions/18891/bagging-boosting-and-stacking-in-machine-learning
2. https://www.quora.com/What-is-bagging-in-machine-learning

