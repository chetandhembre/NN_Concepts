###Regression

```
method of fitting a curve through set of points using some criteria
```
lets consider,

we have sample data about weight of man and their height. We can create model which can find of relation between weight and height. so if any one of them given we can calculate other value.


### Following are important terms in regression

#### 1. Correlation

when we are creating model we consider lot of factors while predicting results. Many times these factors(feature) are so co-related to each other. It means their values are interdependent. 

#####Correlation coefficient

The degree of association is measured by a correlation coefficient, denoted by r. It is sometimes called Pearson's correlation coefficient after its originator and is a measure of linear association. If a curved line is needed to express the relationship, other and more complicated measures of the correlation must be used.

The correlation coefficient is measured on a scale that varies from + 1 through 0 to - 1. Complete correlation between two variables is expressed by either + 1 or -1. When one variable increases as the other increases the correlation is positive; when one decreases as the other increases it is negative. Complete absence of correlation is represented by 0. Figure 11.1 gives some graphical representations of correlation.

#### 2. Least Squares Error: 

this is method use to answer question about how much our model predict answer correctly. Basically it is square of vertical distance between actual point and point predicted by model for given value

![square error graph](http://jmahaffy.sdsu.edu/courses/s00a/math121/lectures/leastsquares/images/bestfit.jpg)

our model should have least square error among all possible model for given data

#### 3. Outliers and Influential Observations

After a regression line has been computed for a group of data, a point which lies far from the line (and thus has a large residual value) is known as an outlier. Such points may represent erroneous data, or may indicate a poorly fitting regression line. If a point lies far from the other data in the horizontal direction, it is known as an influential observation. The reason for this distinction is that these points have may have a significant impact on the slope of the regression line.

![outlier and influential observation](http://images.slideplayer.com/18/6175537/slides/slide_23.jpg)

#### 4. Lurking Variables

If non-linear trends are visible in the relationship between an explanatory and dependent variable, there may be other influential variables to consider. A lurking variable exists when the relationship between two variables is significantly affected by the presence of a third variable which has not been included in the modeling effort. Since such a variable might be a factor of time (for example, the effect of political or economic cycles), a time series plot of the data is often a useful tool in identifying the presence of lurking variables.

#### 5. Extrapolation

Whenever a linear regression model is fit to a group of data, the range of the data should be carefully observed. Attempting to use a regression equation to predict values outside of this range is often inappropriate, and may yield incredible answers. This practice is known as extrapolation. Consider, for example, a linear model which relates weight gain to age for young children. Applying such a model to adults, or even teenagers, would be absurd, since the relationship between age and weight gain is not consistent for all age groups.




#### Type of Regression
1. Linear regression
2. Logistic regresion
3. Ridge regression
4. lasso regresion
5. Ecologic regression
6. Logic regression
7. Bayesian regression
8. Quantile regression
9. LAD regression
10. Jackknife regression

#### Reference
1. [this article](http://www.stat.yale.edu/Courses/1997-98/101/linreg.htm)

