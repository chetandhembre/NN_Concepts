### Vector Norm


#### What is Norm?

before start with vector norm lets first understand what is norm.

```
Norm is function which assign "positive" real value to that describe as length or size of vector.
```

- area of square
- length of line

#### What is vector norm?

lets consider,

x = [x1, x2, x3, ..... , xn]

norm of x can be denoted by ||x||

#### Formula

``` 

|| X ||p =  pow(sum(pow(xi, p)), 1 / p)

```

#### example
1. L1 norm - 
   
   ```
   c = |x1| + |x2| + ... |xn|
	```
	
	if we plot graph for L1 norm it will be look like 
	![l1- norm graph](http://polymathprogrammer.com/images/blog/201003/l1normsquare.png)
	
	x and y from image can be consider as point from vector X
	

2. L2  Norm- 
   
   ```
	c = pow(sum(pow(Xi, 2)), 2)
	```
	![L2 norm](https://inst.eecs.berkeley.edu/~ee127a/book/login/Images/vecs_eucl_norm.png)  
	
	basically L2 norm is equation of circle
	
L1 and L2 are most popular vector norm present. They helps in regularization of neural network

#### Properties
1. || x ||  > 0
2. || k * x || = k * || x || when k is scalar
3. || x + y || <= || x || + || y || 

####Special Case

1. where p is `infinity`

	```
	|| X || infinity = max(xi)
	```

2. where p is `0`

  when p is 0 then it explain cardinality of vector. There are other cases but I am ingoring them doe simplicity
  

#### Why different form of norm?
###ToDO


####Reference
1. [wikipedia](https://en.wikipedia.org/wiki/Norm_(mathematics)#Hamming_distance_of_a_vector_from_zero)
2. [wolfman](http://mathworld.wolfram.com/VectorNorm.html)