we have different way to find out mean of given distribution. Where to use which mean method is problem.

### When to use arithmetic/geometric/harmonic Mean?

The basic idea of mean is the number that represent set of number, and produces same result of original numbers. Which mean to use is totally depend on how these number related/interact with each others.

#### [Arithmatic Mean](https://github.com/chetandhembre/NN_Concepts/blob/master/utils/Arithmatic%20mean.md):
* data is not skewed
* individual data points are not depedent on each other

Example: 
1. lets consider `n` instances we travel a fixed time `t` at velocities v1, v2, v3, .., vn over distance d1, d2, d3,..., dn. Now we want distance covered. Suppose we want to find out what is velocity I should travel for given time `t` for `n` instance so that I will conver same distance as by travelling v1 to vn velocity. That can be calculated by arithematic mean
```
arithmatic mean v = (v1 + v2 + ... + vn) / n
```
2. consider another example where one company's profile grow over last three year by 10 millions, 12 millions and 14 millions. Then we can say we can company's average profite grow is 12 millions every year.

So the additive structure we are trying to maintain is proportional to the measurements we have, so we use arithmetic mean


#### [Geometric Mean](https://github.com/chetandhembre/NN_Concepts/blob/master/utils/geometric%20mean.md)
Example
1. lets consider our company's profit example again, if we say company grow over last three years by 2.5%, 3% and 3.5%, and we want to decide how much avergage percentage by which company grow over three year we can not use `arithmatic mean` here but why not?

Suppose company started with with 100000 profit and then grow for next three year as per above figures. then total profit of company after three years will be

```
100000 * 1.025 * 1.03 * 1.035 = 109270.125
```

if we use arithmatic mean here

```
100000 * 1.03 * 1.03 * 1.03 = 109272.7
```

both results are different. here we should use the geometric mean of growth. 
2. Suppose we have constructed n-dimensional box with given volumn V then
```
V = x1 * x2 * x3 * ... * xn
```
and suppose we wanted to construct n-dimensional cube with same volume v. That is we will replace individual side xi with X.
```
X = (x1 * x2 * ... * xn) * (1/n)
```

use we multiple numbers together to get results when we should use geometric mean


#### [Harmonic Mean](https://github.com/chetandhembre/NN_Concepts/blob/master/utils/harmonic%20mean.md):
Example
1. lets consider velocity-distance-time example again. Now keep distance travel in `n` instance constant and `t` is different for every instance. In this case if we want to figure out velocity with which we should go to cover same distance in `n` instance for `t` time be

```
mean_v = n / (1 / v1 + 1 / v2 + ... + 1 /vn)

```

So we the reciprocal of numbers add up we use harmonic mean.
another important usecase for `harmonic mean` is when 
* a large populartion when the majority of the values are distributed uniformly but where there are few outlier with significant higher values


####Reference
1. http://stats.stackexchange.com/questions/23117/which-mean-to-use-and-when
2. http://mathforum.org/library/drmath/view/69480.html
3. http://economistatlarge.com/finance/applied-finance/differences-arithmetic-geometric-harmonic-means
   

