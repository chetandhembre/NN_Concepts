### Overfitting and Underfitting
***

#### Overfitting
Overfitting is problem neural network face because of lack sufficient training data. 

Here is simple example of `Overfitting`

```
lets say we have neural network which we are training to find `even` number from dataset. Lets consider we train our network on [1, 2, 3, 4, 5, 6]. We ran network on given data for multiple time, network might remember [2, 4, 6] as even number and all other number are non even. This scenario will give us very good result on above training data, but when we try to use network on other dataset where we have say [8, 9, 10, 11, 12] it will classify these number as odd because how network remember data.

```
 from above example it is quit clear effect of Overfitting on our neural network.
 
Usually every unit in NN represent some features of data. If we train NN on small data for large number of epoch. Many such unit co-operate which each other to represent features relation which may not present in actual data.

##### Features
- model fit data too well.
- High [Variance error](https://github.com/chetandhembre/NN_Concepts/blob/master/utils/bias%20variance%20tradeoff.md#variance-error) is reason behind overfitting.
- nerual network represent very complex function.
- neural units come togethor to represent very complex feature of data which is actually not present. Individual unit can not represent feature on their own.


![overfit explained](http://www.holehouse.org/mlclass/10_Advice_for_applying_machine_learning_files/Image%20[8].png) 

above graphs explains us `Overfitting`

![Overfitting error function](http://learning.cis.upenn.edu/cis520_fall2009/uploads/Lectures/overfitting.png)

above graph explain how `Overfitting` causes bad performance on testing time but very good performance on training time.

##### Solution for Overfitting
- stop training when performance on validation set start getting worse
- use regularizers like L1, L2, maxnorm or Dropout
- use soft weight
- use data augmentation to really mix up data so that neural network wont create any false relation. It is very useful when you have very less amount of training data

 
#### Underfitting

Underfitting is another very important problem we face while training our nerual network.

this is occures when our neural network do not fit data too well.
When some of features of data only get learned and gets more importance which in turn reduce performance of model.

#### Features
- do ***not*** fit data well
- High [Bias error](https://github.com/chetandhembre/NN_Concepts/blob/master/utils/bias%20variance%20tradeoff.md#bias-error).
- nerual network become very simple function. such that it only consider part of features from data.


#### Solution for underfiting
- usually by increasing number of hidden layer in neural network.. we can reduce hign bias error and underfitting problem.


