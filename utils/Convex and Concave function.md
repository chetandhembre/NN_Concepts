###Convex and Concave function
***

#### Convex Function
```
a real-valued function defined on an interval is called convex (or convex downward or concave upward) if the line segment between any two points on the graph of the function lies above or on the graph
```

![convex function](https://upload.wikimedia.org/wikipedia/commons/c/c7/ConvexFunction.svg)

- from above graph it is clear that slop at any point interval between `x1` and `x2` continousely increasing.

##### Defination

Let  X be a convex set in a real vector space and let f : X → R be a function.

- f is called convex if:
    x1, x2 belong to X. t belong to [0, 1] then `f(t * x1 + (1 - t) * x2) <= t * f(x1) + (1 - t) * f(x2)`

- f is called strictly convex if:
   x1 != x2,  t belong to [0, 1] then `f(t * x1 + (1 - t) * x2) < t * f(x1) + (1 - t) * f(x2)`    
- f is strictly convex only of (-f) is strictly concave
 
#### Properties
- f(x) is convex function then f''(x) > 0
- Any local minimum of a convex function is also a global minimum. A strictly convex function will have at most one global minimum.
- The additive inverse of a convex function is a concave function.
- If f is concave and g is convex and non-increasing, then h(x)=g(f(x)) is convex.

#### Examples
-  f(x)=|x|^p for 1 ≤ p is convex.
-  f(x)=|x| is convex, but not strictly convex, does not have derivative at 0
-  f(x) = e ^ x is convex
-  every [norm](https://en.wikipedia.org/wiki/Norm_(mathematics)) is convex function


***Convex functions play an important role in many areas of mathematics. They are especially important in the study of optimization problems where they are distinguished by a number of convenient properties***


#### Concave Function
```
a real-valued function defined on an interval is called concave if the line segment between any two points on the graph of the function lies under or on the graph

```

![concave function](https://upload.wikimedia.org/wikipedia/commons/7/73/ConcaveDef.png)

##### Defination

Let  X be a convex set in a real vector space and let f : X → R be a function.

- f is called concave if:
    x1, x2 belong to X. t belong to [0, 1] then `f(t * x1 + (1 - t) * x2) >= t * f(x1) + (1 - t) * f(x2)`

- f is called strictly concave if:
   x1 != x2,  t belong to [0, 1] then `f(t * x1 + (1 - t) * x2) > t * f(x1) + (1 - t) * f(x2)`    
- f is strictly concave only of (-f) is strictly convex

##### Properties
- A differentiable function f is concave on an interval if and only if its derivative function f′ is monotonically decreasing on that interval, that is, f''<0: a concave function has a decreasing slope.
- Any local maximum of a concave function is also a global maximum. A strictly concave function will have at most one global maximum.
- Near a local maximum in the interior of the domain of a function, the function must be concave; as a partial converse, if the derivative of a strictly concave function is zero at some point, then that point is a local maximum.


##### Example
- f(x) = - x ^ 2.
- g(x) = square_root(x).
- f(x) = log(x) when 0 <= x <= infinity.
- The sine function is concave on the interval [0,pi].
- f(x) = log|x| is concave.


#### Inflection Point

```
point in curve where curve become convex function to concave function or vice versa.
```

![inflection point](https://upload.wikimedia.org/wikipedia/commons/7/78/Animated_illustration_of_inflection_point.gif)


from above graph it is clear that at inflection point curve is in transition from concave to convex or vice versa.

#### Inflection points sufficient conditions:

- A sufficient existence condition for a point of inflection is:
	If f(x) is k times continuously differentiable in a certain neighbourhood of a point x with k odd and k ≥ 3, while f(n)(x)=0 for n = 	2,...,k - 1 and f(k)(x) ≠ 0 then f(x) has a point of inflection at x.
- Another sufficient existence condition requires f′′(x + ε) and f′′(x - ε) to have opposite signs in the neighborhood of x , if also a tangent exists here. 


#### Refernce
1. [wikipedia - convex](https://en.wikipedia.org/wiki/Convex_function)
2. [wikipedia - concave](https://en.wikipedia.org/wiki/Concave_function)
3. [wikipedia - inflection point](https://en.wikipedia.org/wiki/Inflection_point)