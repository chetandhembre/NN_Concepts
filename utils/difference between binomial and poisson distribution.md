#difference between binomial and poisson distribution


###Binomial Distribution
 are useful to model events that arise in a binomial experiment, Examples include how many coin flips show heads, how many scratch-off lottery tickets are winners, how many of a doctor's patients die during surgery, and how many free throws I make in one hundred attempts.  Key ingredients of such an experiment include:

- A fixed number of repeated, identical, independent trials.  n is usually the parameter chosen to label the number of trials.
- Every trial results in either a success, with probability p, or a failure, with probability 1-p.  These must be the only two outcomes for a trial.
- The random variable of interest is the total number of trials that ended in a success.

The probability mass function for the binomial distribution is given by:
```
p(x)=(nx)px(1−p)n−xp(x)=(nx)px(1−p)n−x  for  x=0,1,2,…,nx=0,1,2,…,n 
```

###Poisson distributions
are useful to model events that seem to take place over and over again in a completely haphazard way.  For example, how many magnitude 8+ earthquakes will take place in a particular year?  Or, how many babies will be born in a large hospital on a particular day?  Or, how many hits will a website get in a particular minute?  Key assumptions for the Poisson model include:
- The random variable counts the number of events that take place in a given interval (usually of time or space)
- All events take place independently of all other events
- The rate at which events take place is constant usually denoted  λ 

The probability mass function is given by:

```
p(x)= e^−λt * (λt)^x / x! for x=0,1,2,…x=0,1,2,…

```


###Source
- https://www.quora.com/Probability-statistics-What-is-difference-between-binominal-poisson-and-normal-distribution
