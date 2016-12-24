### Chain Rule

#### Formula
```
y = f(g(x))

 dy       df         dg
----  =  ----   *  -----
 dx       dx         df
```


this is one of most important thing in understanding derivatives.

At nutshell we derivative is change in system.

Consider train decreased speed from 50 km/s to 20 km/s as it approaches to station. So we can say dv(change is speed of train) is 30 km/s. In this example we try to understand change in velocity with respect to time.

No consider following system


![chain rule system](https://betterexplained.com/wp-content/uploads/derivatives/chainrulelink.png)


from image it is clear that x, f, g and y are interconnected to each other.

so output of `x` goes to `f` whose output use as input to `g` and so on.

important things to know here is `g` do not know `x` is present in system and vice versa. same with `f` and `y`.


Chain rule helps us to understand how much change in `x (dx)` affect change in `y (dy)`

lets go step by step and answer following question

1. Give me change in `f` due to dx

	```
	df = dx * (df / dx)
	```
	
	dx is input.. and per change in f unit due to per x unit

2. Give me change in `g` due to df
   
   ```
   dg = df * (dg / df)
   ```

3. Give me change in `y` due to dg

   ```
   dy = dg * (dy / dg)
   ```

4. How much changes in x (dx) affect in changes in y (dy)

   ```
   dy = df * (dg / df) * (dy / dg)    - substituted dg
   
   dy = dx * (df / dx) * (dg / df) * (dy / dg)    - substituted df

     dy         df       dg        dy
   ----   =   ----  *  ----  *   ----
     dx         dx       df        dg  
   ```
 
Now we can see direct effect of x on y and that is chain rule for you.

It helps you to understand impact on output from direct or indirect input. 

#### Example

consider

```

y = g(f(x))

where f(x) -> x^2
      g(f) -> f ^ 3

now we want to figure out how change in x will affect change in y

 dy      d(g(f(x)))       dg      df
---- =  ------------  =  ---- *  -----
 dx         dx            df      dx
 
 
 df / dx = d(x^2) = 2x
 dg / df = d(f^3) = 3 * f^2 = 3 * (x^2)^2 = 3x^4
 
 dy / dx = 2x * 3x^4 = 6x^5
```


#### Reference
- [better explaiend](https://betterexplained.com/articles/derivatives-product-power-chain/)