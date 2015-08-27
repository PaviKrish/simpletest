from stats import mean, std
from nose.tools import assert_equal
from nose.tools import assert_almost_equal 
def test_mean():
	assert_almost_equal(mean([2,4]), 3)
	#print mean([2,4])
#test_mean()
def test_float_mean():
	assert_almost_equal(mean([1,2]),1.5)
#test_float_mean()
def test_neg_mean():
	assert_almost_equal(mean([-2,-4]), -3)
test_neg_mean()
def test_mixed_mean():
	assert_almost_equal(mean([-4,4]), 0)
#test_mixed_mean()	
def test_std1():
	obs =std([0.0,2.0])
	exp = 1.0 
	assert_equal(obs,exp)
