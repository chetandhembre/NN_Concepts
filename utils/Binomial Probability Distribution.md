#Binomial Probability Distribution

##When?
- The experiment consists of n repeated trials.
- Each trial can result in just two possible outcomes. We call one of these outcomes a success and the other, a failure. (thats by binomial)
- The probability of success, denoted by P, is the same on every trial
- The trials are independent; that is, the outcome on one trial does not affect the outcome on other trials.

##Notation
- x: The number of successes that result from the binomial experiment.
- n: The number of trials in the binomial experiment.
- P: The probability of success on an individual trial.
- Q: The probability of failure on an individual trial. (This is equal to 1 - P.)
- n!: The factorial of n (also known as n factorial).
- b(x; n, P): Binomial probability - the probability that an n-trial binomial experiment results in exactly x successes, when the probability of success on an individual trial is P.
- nCr: The number of combinations of n things, taken r at a time

##Formula
```
b(x; n, P) = nCr * P^x * (1 - P)^x
```

```
The binomial probability refers to the probability that a binomial experiment results in exactly x successes
```

##Properties
- The mean of the distribution (μx) is equal to n * P.
- The variance (σ2x) is n * P * ( 1 - P ).
- The standard deviation (σx) is sqrt[ n * P * ( 1 - P ) ].


##Source
-http://stattrek.com/probability-distributions/binomial.aspx
