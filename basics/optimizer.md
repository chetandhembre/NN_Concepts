### Optimizer
***

Single most important goal of optimizer is to find `W` such that it will minimize loss function.

if we plot graph error on verticle axis and weight on horizontal axis we will get following graph.

![loss graph againt weight](https://dmm613.files.wordpress.com/2014/12/convex_cost_function.png)

this is most simplest form of graph for understanding,

- verticle section of graph is parabolas
- horizontal section of graph is ellipses

So what optimizer do it to start from one of then outermost edge of ellipses and try to reach global minima (which is most of local minima). This is explained is following graph.

![elliptical graph](http://aria42.com/images/steepest-descent.png)

so we are at `x0` and trying to reach at center of ellipses. 

#### Types of Optimizer

##### 1. Random Search

In this method we try to assume some random values for `W` and see of it minimize loss function.
We can see how many things are wrong with method.

##### 2. Random Local search.

We choose next value of `W` but selecting random local values and see if these values helps us to go downhill. 
Concretely, we will start out with a random W, generate random perturbations δW to it and if the loss at the perturbed W+δW is lower, we will perform an update.
It is not most efficient way to solve problem.

##### 3. Follow Gradient

- we can compute the best direction along which we should change our weight vector that is mathematically guaranteed to be the direction of the steepest descend (at least in the limit as the step size goes towards zero). 
- Gradient means `derivatives`, and if we have vector of these number we call derivative as `partial derivatives`


##### Gradient Descent
```
procedure of repeately evaluating gradient and then performing a parameter update is called gradient descent.
```

There different ways to do gradient descent depending on efficiency and time of calculations.

##### 1. Batch Gradient Descent

- compute gradient for whole training dataset once.
- `W = W - learning_rate * gradient`.
- once update to perform gradient for whole dataset.
- We have to store all data in memory to perform it. So it is expensive.
- Computing gradient for all training data set is slow. So we can not do it online.

##### 2. Stochastic Gradient Descent (SGD)

- It is another extrem than batch gradient descent.
- Calculate and update gradient for every training point.
- For example for given training data point x and y
   `W = W - learning_rate * gradient(W, x, y)`
- It is less expensive and fast process.
- We can do gradient update online.
- SCG perform gradient update more frequently with high variance which might lead to fluctuation of objective function.
- This might lead to gradient descent jumps to local minima. And can not overshoot objective function.
- By schedule decreasing learning_rate SGD can surely reach local minima but it might take some time.

![SGD fluctuation](http://sebastianruder.com/content/images/2016/09/sgd_fluctuation.png)

[***fluctuation of SGD***]

##### 3. Mini Batch Gradient Descent

- You guess it right, It is mid ground between Batch and Stochastic gradient descent.
- Instead of calculating gradient for whole training data set we calculate gradient for some batch of dataset, which we can store it in memory easily, so it is faster.
- We are not performing update some small batch of training data point instead of every single on individually, mini batch becomes less expensive than SGD and fast we can do `online` update.
- It do not update gradient as much as SGD, so it wont create any high variance in objective function.


##### Challanges in Mini Batch Gradient Descrent

- choosing learning rate is as issue. Small learning rate means slow learning and Large learning rate means overshooting and fluctuation.
- There is not way to change learning rate on the fly. Means if we are see some infrequent update we can increase learning rate and small learning rate for more frequent updates.
- Same learning rate applys to all hidden layer independent on data.

#### Thoughts of Learning rate
- It is important hyper parameter while training neural network.
- It inidicate how much penalty(/learning) we will take given error.
- High Learnign rate means we will decrease our weight by large margin, and we will start taking large step which might cause to miss minima.

![high learning rate](http://www.turingfinance.com/wp-content/uploads/2014/05/High-Learning-Rate1.gif)

- Small learning rate means, we will take lot of time to reach minima.

![low learning rate](https://wingshore.files.wordpress.com/2014/11/alpha1.png)

from above image it is clear that, with small learning rate we take very small step even we know we are going to steepest direction.

- Here is summary of `effect of learning rate`

![learnign rate effect](http://cs231n.github.io/assets/nn3/learningrates.jpeg)


#### Solution for Gradient Descent challanges

##### 1. Momentum

Momentum try to avoid increasing overshooting of objective function as increase in learning rate. So we are trying to perform gradoent update very quickly by increasing learning rate but it avoid overshooting objective function.

- Momentum can be explained more precisely in physics term.
- Lets consider objective function is at edge of convex function. It has height `h` from horizontal surface which means it has some potential energy.
- When we update gradient we are simply setting thing in motion, which convert potential energry to kinetic energy so we have momentum.
- in subsequent update due to high learning rate we try to more thing in next steepest descent. But as thing has momentum in original direction. So resultant direction will be vector addition of current direction of thing and new gradient update.

![momentum gradient update](http://blog.wtf.sg/wp-content/uploads/2014/05/Screenshot-from-2014-05-25-145500.png)

```

Vt = lambda * Vt-1 - learning_rate * dx

W = W + Vt

where,
lamba - coefficient of momentum, 
1 - lambda is coefficient of friction
```

from above equation it is clear than if lambda is high then we have much faster gradient descent.

So we follow these steps
- we start lambda with `0.5` while we have high gradient
- then we increase it to `0.9` as large gradient disappered


##### 2. Nestrov Momentum
#TODO



#### Annealing the learning rate

one of challange we have with normal mini batch gradient descent is, we have to use same learning rate whole time while training. So if we have large learning rate our model will fluctuate a lot and wont settle on minima. If learning rate is small then it take lot of time to reach minima. It means we are wasting so much computation. 

Annealing of learning is one of way to solve this problem. In Annealing we start with high learning rate and as training progresses we reduce learning rate.

Followings are way to do it
##### 1. Step decay
- Reduce the learning rate by some factor every few epochs.
- Typical values might be reducing the learning rate by a half every 5 epochs, or by 0.1 every 20 epochs.These numbers depend heavily on the type of problem and the model.
- One heuristic you may see in practice is to watch the validation error while training with a fixed learning rate, and reduce the learning rate by a constant (e.g. 0.5) whenever the validation error stops improving.

##### 2. Exponential decay
- mathematical form α=α0e−k, where α0,k are hyperparameters and tt is the iteration number (but you can also use units of epochs).

##### 3. 1/t decay
-  the mathematical form α=α0/(1+kt) where a0, k are hyperparameters and t is the iteration number.

***step decay dropout is more preferable in practice***

##### Per-parameter adaptive learning rate methods

Till know we have to use `learning_rate` hyper-parameter and tune to achieve good results. It is very hard and time consuming task. Following are few methods where we do not have to manage `learning_rate`.

##### 1. Adagrad

SGD does not allowed us to change learning_rate depend on type of data/feature we are trying to update. And this really is an issue.

- In `Adagrad`, we use high learning rate (means large update) for infrequent updates. And small learning rate for frequent updates.
- It works very well with sparse data.

```
cache = dx ** 2

        - learning_rate 
x += --------------------  *  dx
      np.sqrt(cache) + e
       
where, 
cache -  is buffer where we store record of gradient updates. It is shape of dx
e - smoothing parameter, typically value is 1 * e^-4 to 1 *  e^-8

```

##### Problems
1. In large learning rate, monotonose learning rate proves to be more aggresive and learning can stop early.

##### 2. Adadelta
#TODO

##### 3. RMSprop
- So problem with Adagrad is it causes to decrease learning rate rapidally, and RMSprop try to solve it.
- Solution for this problem is instead of storing all gradient in cache, we select part of it. So even if we suddenly encounter large gradient update we smooth is out.

```

cache = decay_rate * cache + (1 - decay_rate) * dx ** 2

        -  learning_rate
x += ---------------------- * dx
       np.sqrt(cache) + e
       
where, 
decay_rate is hyper-parameter [0.9, 0.99, 0.999]
e - smoothing parameter [e^-4 to e^-8]
```
- cache parameter is leaky here because we not considering all value for calculating new cache.
- updates are not monotonical


##### Adam

- RMSprop + momentum.
- store decaying square of gradient in cache like RMSprop.
- store decaying gradient in momentum like momentum.

```
m = beta1 * m + (1 - beta1) * dx

v = beta2 * m + (1 - beta2) * dx ** 2

where, 
beta1 and beta2 are hyper-parameter
beta1 - 0.9
beta2 - 0.999
```

***It perform better than default RMSprop alog***

`m` and `v` are initialize to zero so they biased toward 0 especially during initial step when `Beta1` and `Beta2` are close to 1.

So avoid bais toward 0 we correct bais by performing following

```

m = beta1 * m + (1 - beta1) * dx

v = beta2 * m + (1 - beta2) * dx ** 2

           m
m =   ------------
       1 - beta1
    
           v
v =   ------------
       1 - beta2
       
          - learning_rate
x +=   ---------------------- * m
            np.sqrt(v) + e
          
where,
beta1 and beta2 are hyper-parameter
beta1 - 0.9
beta2 - 0.999
e - smoothing factor
```

- it uses smoothing gradient like `m` instead of row gradient. It helps to avoid rapid increase in gradient.


####Visualizing Algorithm
![gradient descent](http://sebastianruder.com/content/images/2016/09/contours_evaluation_optimizers.gif)


if you look carefully `Adagrad`, `Adadelta` and `RMSprop` converges to minima very fast. Momentum and NAG initially went to another part but eventually reach required minima.

`SGD` was so slow.


![gradient descent](http://sebastianruder.com/content/images/2016/09/saddle_point_evaluation_optimizers.gif)

above gif showing how various gradient descent algorithm behave on [`saddle point`](https://github.com/chetandhembre/NN_Concepts/blob/master/utils/saddle%20point.md). 

`Adagrad`, `Adadelta` and `RMSprop` handle saddle point pretty well.
`Momentum` and `NAG` took lot of time because of their initial momentaum was not direction of gradient.
`SGD` unable to come out of `saddle point` may be because of step size is too small to come out of local minima.


#### Which Optimizer to choose?

`SGD` is so slow and we have to set proper learning rate while training.
If our data is sparse then we can use `Adagrad`, `Adadelta` or `RMPprop`, among these three I will prefer to use `RMPprop` as it works in mini batch as well as It's learning rate does not decrease as drastacaly as 	`Adadelta`.
`Adam` provide us speed of `Moementum` and learning rate anneling for `RMSprop`, So it is better choice than others.

***Adam is very good choose for optimizer***



#### Reference
1. [this excellent article](http://sebastianruder.com/optimizing-gradient-descent/index.html#whichoptimizertochoose)
2. [cs231n notes](http://cs231n.github.io/neural-networks-3/#update)
3. [Neural Networks for Machine Learning week 6 - coursera](https://www.coursera.org/learn/neural-networks/home/week/6)
