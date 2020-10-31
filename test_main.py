import unittest
import inspect
from main import *

class UnitTests(unittest.TestCase) :
    def test_statistic(self) :
        self.assertTrue( np.abs( sum(data) - statistic(data) ) <1e-7, "the statistic is not being computed correctly by your function" )
    
    def test_criticalRange(self) : 
        l = scipy.stats.binom.ppf(0.025,20,1/3 )
        u = scipy.stats.binom.ppf(0.975,20,1/3 )
        lll, uuu = criticalRange( 1/3, len(data) )
        self.assertTrue( np.abs(l-lll)<1e-4, "the lower bound for the critical region has been computed wrongly" )
        self.assertTrue( np.abs(u-uuu)<1e-4, "the upper bound for the critical region has been computed wrongly)

   def test_hypothesisTest(self) :
       hhh = hypothesisTest( data, 1/3 ) 
       self.assertTrue( hhh=="there is insufficient evidence to reject the null hypothesis", "the phrase returned by hypothesisTest" )
       self.assertTrue( inspect.getsource(hypothesisTest).find("if")>0, "your hypothesisTest function does not return an if"  )
       self.assertTrue( inspect.getsource(hypothesisTest).find("the null hypothesis is rejected in favour of the alternative")>0, "the hypothesis test function does not contain the string "he null hypothesis is rejected in favour of the alternative."  This string should be present and output when the sample mean falls inside the critical region." ) 
