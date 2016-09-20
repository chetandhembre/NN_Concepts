#Poisson Distribution

A Poisson random variable is the number of successes that result from a Poisson experiment. The probability distribution of a Poisson random variable is called a Poisson distribution.

##formula
```
P(x; μ) = (e^-μ) (μ^x) / x!
```

where
- μ: mean number of success occured
- x: actual number of successes that occur
- e: A constant equal to approximately 2.71828.
- P(x; μ): The Poisson probability that exactly x successes occur in a Poisson experiment, when the mean number of successes is μ.

##Application
1. the event is something that can be counted in whole numbers
2. occurrences are independent, so that one occurrence neither diminishes nor increases the chance of another
3. the average frequency of occurrence for the time period in question is known
4. it is possible to count how many events have occurred

```
poisson distribution generally tells about randomness of event. So we only consider occurence pobability of event and not absent of it.
```

##Example
The average number of homes sold by the Acme Realty company is 2 homes per day. What is the probability that exactly 3 homes will be sold tomorrow?

Solution:

This is a Poisson experiment in which we know the following:

- μ = 2; since 2 homes are sold per day, on average.
- x = 3; since we want to find the likelihood that 3 homes will be sold tomorrow.
- e = 2.71828; since e is a constant equal to approximately 2.71828.

We plug these values into the Poisson formula as follows:
```
P(x; μ) = (e-μ) (μx) / x!

P(3; 2) = (2.71828-2) (23) / 3!

P(3; 2) = (0.13534) (8) / 6

P(3; 2) = 0.180
```
Thus, the probability of selling 3 homes tomorrow is 0.180 .

##Summary
- The Poisson distribution deals with mutually independent events, occurring at a known and constant rate r per unit (of time or space), and observed over a certain unit of time or space.
- The probability of k occurrences in that unit can be calculated from p(k) = (μ^k) * (e^μ) / (k!).
- The rate r is the expected or most likely outcome (for whole number r greater than 1, the outcome corresponding to r-1 is equally likely).
- The frequency profile of Poisson outcomes for a given r is not symmetrical; it is skewed more or less toward the high end.

##Source
- http://stattrek.com/probability-distributions/poisson.aspx
- https://www.umass.edu/wsp/resources/poisson/
