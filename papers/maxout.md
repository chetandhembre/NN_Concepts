## Maxout

Paper [link](https://arxiv.org/pdf/1302.4389v4.pdf)

### Authors
* Ian J. Goodfellow 
* David Warde-Farley
* Mehdi Mirza 
* Aaron Courville
* Yoshua Bengio

####Motivation

as we know `dropout` can help use to avoid overfiting and achieve about 10% improvement over non dropout neural network.

Maxout is specifically built to play well with `dropout` so that overal gain will be more.

```
maxout is activation function
```

if you see normal activation function like `relu`. These are linear functions. In order to cover more complex non-linear shape we can create lots of linear function togethor.

![non-linear-linear](http://www.simon-hohberg.de/assets/approximation.svg)

from above diagram we can say that we can represent complex non-linear activation function with multiple linear function, each will learn unique features.

But problem with using multiple linear activation function in single NN. It will create lots of parameter with small training data set becomes `overfiting`.

But hey dropout help us to avoid overfiting so lets use maxout with dropout for better performance.

```

x belongs to R(d), a maxout hidden layer implementation wil be

hi(x) = max(j belong [1, k]) * zij

zij = xTW..ij + bij

W belong to R(d x m x k)
b belongs to R(m x k)
```


