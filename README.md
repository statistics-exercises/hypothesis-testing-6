# Hypothesis tests for Bernoulli random variables

You have now done a couple of hypothesis tests and that we have also started to look at some of the theory.  You should thus be getting a bit more comfortable with this flowchart:

![](hypo-testing.001.jpeg)

Thus far we have performed hypothesis tests for samples taken from normal distributions.  In this exercise, by contrast, we are going to suppose that we are gambling against a character with dubious morals.  We are playing a game which we have fixed odds of winning with this reprobate and we have a suspicion that he may have lied to us when he told us these odds.  What, therefore, can we do to test if our suspicions are correct or not?

Let's suppose that our probability of winning each game is we place 1/3 and the outcomes for the first 20 games we have played are given in the file `games.dat`.  The ones in this file indicate the games that we won and the zeros the ones we lost.  Can we do a hypothesis test with this data?

To answer this question we need to recognise that each of the ones or zeros in `games.dat` is a __Bernoulli random variable__.  The sum of all these numbers is thus a __binomial random variable__.  We can thus set up our __null and alternative hypotheses as follows__:    

1. __null hypothesis__: the probability of winning is 1/3
2. __alternative hypothesis__: the probability of winning is not 1/3

Our statistic is then going to be the sum of all the random variables, which under the assumption of the __null hypothesis__ is a sample from a __binomial random variable__ with p=1/3 and n=20.  We now use this information to determine the __critical region__ for a 5% __significance level__.  If we were doing this by hand we would use the New Cambridge statistical tables here.  In python, however, we can use the following function to extract the fifth percentile for a binomial random variable with n=20 and p=1/3:

````
per = scipy.stats.binom.ppf(0.05, 20, 1/3)
````

The final step is then, of course, to determine whether the __statistic__ falls within the __critical region__ and to thus decide whether the __null hypothesis__ should be rejected or not.

__Your task now is to write a code to perform this hypothesis test within Python.__  I have written an outline set of functions for you to get you started.  In particular:

1. `statistic` - takes a numpy array called `data` in input.  This array contains the results for the games that have been played.  It should return the value of the __statistic__.
2. `criticalRange` - takes two arguments `p` and `n`.  These two quantities are the p and n parameters for the binomial distribution that it is assumed the __statistic__ is sampled from under the assumption of the __null hypothesis__.  The function should return two variables `lower` and `upper`.  The variable `lower` should be set so that the probability (under the null hypothesis) the __statistic__ is less than or equal to this value is 2.5%.  The variable `upper` should be set so that the probability (under the null hypothesis) the __statistic__ is less than or equal to this value is 97.5%.
3. `hypothesisTest` - this function takes two arguments.  `data` is the list of datapoints from the input file, `p` is the probability of winning that is assumed under the __null hypothesis__.  The `criticalRange` function is called within this function.  To complete the task you must use the values returned from this function as well as the value of the __statistic__ to write an if statement that determines whether the statement "_the null hypothesis is rejected in favour of the alternative_" should be returned or whether the statement "_there is insufficient evidence to reject the null hypothesis_" should be returned.  


   
