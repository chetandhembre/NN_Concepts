####Expected Value (u)

Expected Value is mean value of infinit population.

Population has to be finit inorder to calculate mean of it. But sometime it is not always case.

`Expected Value` help us to find out mean of infinit population given it's probability distribution is given.

Lets consider X is our population, P represent probability distribution of element from it. Then 

```
E(X) = sum( x * P(x) )
E(X) - Expected Value of Population X
x - individual element of X
P(x) is probability of x occurance in X

```
##### Example

Lets consider we have population X with following elements and their probability of occurance in population.

|   x  |   1  |   2   |   3   |
|------|------|-------|-------| 
| P(x) |  0.2 |  0.3  |  0.5  |


So E(X) can be calculated as follow by following above formula

```
E(X)  =  1 * 0.2 + 2 * 0.3 + 3 * 0.5
      =  0.2 + 0.6 + 1.5
      =  2.3
```

So what it suggests that when we pick `x` from `X` for n times and average it, we will get `2.3`.

##### Variance (𝞂 ^ 2)

Variance for infinit population can be calculated as,

```
E[(X - u) ^ 2)] = sum( p(x) * (x - u) ^ 2)
```

we can calculated it also by

```
E[(X - u) ^ 2)] = E(X^2) - [E(X)]^2

```

this is more optimized and easy way to calculate it.

####Application

It is very helpful when you have represent system which has different output with different probability of occurance, then `Expected Value` help us to represent this system output with single number.

Here is very simple game example for it, [Youtube Video](https://www.youtube.com/watch?v=DAjVAEDil_Q)

