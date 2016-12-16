###Geometric Mean

The geometric is special type of average where we multiply the numbers together and then take a square root (for two numbers), cube root (for three numbers) etc

####Example
1. What is Geometric Mean of 2 and 18?
	* first multiple them : 2 * 18 = 36
	* then take the square root: sqrt(36) = 6 


2. What is Geometric Mean of 10, 51.2 and 8?
   * first we multiply them: 10 * 51.2 * 8 = 4096
   * then take the cube root: (4096)^1/3 = 16


#### Defination
for `n` numbers: multiply them all togethor and then take the `nth root`

more formally, geometric mean of n numbers a1 to an is
```
x = pow(a1 * a2 * a3 * .... * an, 1\n)
```
 
It is also know as 

```
The average of the logarithmic values of a data set, converted back to a base 10 number.
```

#### Proof
```
x = pow(a1 * a2 * a3 * .... * an, 1\n)

pow(x, n) = a1 * a2 * a3 * .... * an

log(pow(x, n)) = log(a1 * a2 * a3 * .... * an)

nlog(x) = log(a1) + log(a2) + log(a3) + ... + log(an)

log(x) = (log(a1) + log(a2) + log(a3) + ... + log(an)) / n

x = pow(10, (log(a1) + log(a2) + log(a3) + ... + log(an)) / n)
```

#### How to handle zero values?

according to formula of GA.. if we have any of value zero then resultant geometric mean is `0`. But it does not mean we should not calculate GA of values containing zero.

There are three way to handle it,

1. If any value is zero (0), one is added to each value in the set and then one is subtracted from the result.

2. Blank and 0 values are ignored in the calculation.

3. Zero (0) values are converted to one (1) for the calculation.

#### How to handle negative values?
`ToDO`

#### How GA helps in selecting aspect ration?
`ToDo`

#### Reference
* [Math is fun](https://www.mathsisfun.com/numbers/geometric-mean.html)
* http://www.wwdmag.com/channel/casestudies/handling-zeros-geometric-mean-calculation
* http://www.buzzardsbay.org/geomean.htm
