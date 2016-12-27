###Loss Function And Cost Function
In supervise learning we usually have labeled data and we create model which learn to  predict labels correctly.

Process is simple. We first predict label which will be checked against our hand crafted labels and then calculate error of our model.

loss function/cost functions are different way to interpret these error.

Over the preiod of training we want to reduce values of loss(cost) function.

```
x - input
f(x) - model
y1 -  model output
y - correct o/p

loss function is (y1 - y) which tell you error in your function f(x)

```

#### Types of Loss functoin

1. #### Hinge Loss

   ```
   l(y, f(x)) = max(0, 1 - y * f(x))
   ```
   
   ![hinge loss](https://web.archive.org/save/_embed/https://www.researchgate.net/profile/Haoran_Xie/publication/286920509/figure/fig3/AS:306761400635395@1450149025079/Fig-4-The-hinge-loss-function.png)


   - use in SVM classifier (Binary classifier)
   - more you violete the margin the higher the penalty
   - does not go well with regresion model.

   
2. ####Square Error

  ```
  l(y, f(x)) = square(y - f(x))
  ``` 
  
  ![square error image]()
  
  - use in regression problem
  - outlier in data punished very heavily by squaring of the error

3. ####Absolute Error
   
   ```
   l(y, f(x)) = | y - f(x) |
   ```
   ![absoulte error]()
   
   - use in regression problem
   - solve problem with `square error` by scaling loss function linearly.

 
4. ####e - insensitive Loss

    ```   
                  | y - f(x) |  f(x) > e or f(x) < -e
                /
    l(y, f(x)) = 
                \ 0              -e <  f(x) < e
                
                  
    ```
    ![epsilon - insensitive loss](https://web.archive.org/save/_embed/https://www.researchgate.net/profile/Qingsong_Xu4/publication/222536579/figure/fig6/AS:305314453835780@1449804046209/Fig-6-The-curve-of-the-e-insensitive-loss-function.png)
    
    - use for SVM.
    - allowed to have noise in input


5. ####Cross Entropy 
  
	- help you to undestand difference between correct probability distribution and network's output.
  		
	```
	C = - 1 / n * sum(x)[(y * ln(a) + (1 - y) * ln(1-a))]
	
	```
  		
	y's value is either 0 or 1. so value of network's output always (0, 1] then value of C will be in (0, 1]
  		
	- use when network's o/p represent independent hypothesis and node activation can be understand as representing the probability that each hypothesis is true i.e. when you have `softmax` as output layer activation function

  		
6. ####Mean Square Error(MSE)

  ```
  e =  1/n * sum[square(y1 - y)]
  ```
  
  - most famous loss function
  - always position output
  - target is continuous and normally distributed, and you maximize the likelihood of the output of the net under these assumptions


7. #### KL Divergence

  ```
   KL(p || q) = sum(x)[p(x) * ln(p(x) / q(x))]
  ```
  
  - it shows distance between distribution of p and q
  - we consider p as target and q as output from model
  - non negative output
  - KL(p || q) != KL(q || p) i.e. not symmetric
  - when target p is fixed then cross entropy and KL divergence values are same
  
#### TODOS
- softmax loss
- svm loss

 #### When to use what?
 
 - binary classification problem (SVM) - hinge/e - insensitive Loss
 - regresion problem (real number output)- square/absolute/mse
 - probability distribution with target has only one output [0, 1, 0, 0] - cross entropy (softmax function)
 - target is probability distribution - KL divergence
      
      		
  		
     
      
