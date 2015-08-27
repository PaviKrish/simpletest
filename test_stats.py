from stats import mean
from nose.tools import assert_equal_equal  
def test_mean():
	assert_equal(mean([2,4]), 3)
	#print mean([2,4])
#test_mean()
def test_float_mean():
	assert_equal(mean([1,2]),1.5)
#test_float_mean()
def test_neg_mean():
	assert_equal(mean([-2,-4]), -3)
test_neg_mean()
def test_mixed_mean():
	assert_equal(mean([-4,4]), 0)
#test_mixed_mean()	


