#Bootstrap
if we take sample from population and wanted to know how variable (different) data is. there are two options

1. take more samples from population
2. take samples from our sample 

option 1 is sometime no feasible so we now left with option 2. It can be not intuitive, but it can work and this menthod is called bootstraping.

here question and ans from [here](http://stats.stackexchange.com/questions/26088/explaining-to-laypeople-why-bootstrapping-works)

## Question
```
Explaining to laypeople why bootstrapping works

I recently used bootstrapping to estimate confidence intervals for a project. Someone who doesn't know much about statistics recently asked me to explain why bootstrapping works, i.e., why is it that resampling the same sample over and over gives good results. I realized that although I'd spent a lot of time understanding how to use it, I don't really understand why bootstrapping works.

Specifically: if we are resampling from our sample, how is it that we are learning something about the population rather than only about the sample? There seems to be a leap there which is somewhat counter-intuitive.

I have found a few answers to this question here which I half-understand. Particularly this one. I am a "consumer" of statistics, not a statistician, and I work with people who know much less about statistics than I do. So, can someone explain, with a minimum of references to theorems, etc., the basic reasoning behind the bootstrap? That is, if you had to explain it to your neighbor, what would you say?

```

##Answer

```
fwiw the medium length version I usually give goes like this:

You want to ask a question of a population but you can't. So you take a sample and ask the question of it instead. Now, how confident you should be that the sample answer is close to the population answer obviously depends on the structure of population. One way you might learn about this is to take samples from the population again and again, ask them the question, and see how variable the sample answers tended to be. Since this isn't possible you can either make some assumptions about the shape of the population, or you can use the information in the sample you actually have to learn about it.

Imagine you decide to make assumptions, e.g. that it is Normal, or Bernoulli or some other convenient fiction. Following the previous strategy you could again learn about how much the answer to your question when asked of a sample might vary depending on which particular sample you happened to get by repeatedly generating samples of the same size as the one you have and asking them the same question. That would be straightforward to the extent that you chose computationally convenient assumptions. (Indeed particularly convenient assumptions plus non-trivial math may allow you to bypass the sampling part altogether, but we will deliberately ignore that here.)

This seems like a good idea provided you are happy to make the assumptions. Imagine you are not. An alternative is to take the sample you have and sample from it instead. You can do this because the sample you have is also a population, just a very small discrete one; it looks like the histogram of your data. Sampling **'with replacement'** is just a convenient way to treat the sample like it's a population and to sample from it in a way that reflects its shape.

This is a reasonable thing to do because not only is the sample you have the best, indeed the only information you have about what the population actually looks like, but also because most samples will, if they're randomly chosen, look quite like the population they came from. Consequently it is likely that yours does too.

For intuition it is important to think about how you could learn about variability by aggregating sampled information that is generated in various ways and on various assumptions. Completely ignoring the possibility of closed form mathematical solutions is important to get clear about this.
```


important things while taking sample from sample it we have to use sampling [`with replacement`](https://raw.githubusercontent.com/chetandhembre/NN_Concepts/master/utils/Sampling%20With%20Replacement%20and%20Sampling%20Without%20Replacement.md). So what it means that we can have same data point multiple time in our sample and same time we wont have all data point from origin sample.
So we check for variance of data over our derived samples (sampled from original sample). And for some type of data it is same as original population.

##source
- http://stats.stackexchange.com/questions/26088/explaining-to-laypeople-why-bootstrapping-works
- http://www.burns-stat.com/documents/tutorials/the-statistical-bootstrap-and-other-resampling-methods-2/
