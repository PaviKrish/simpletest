from stats import mean 
def test_mean():
	assert(mean([2,4]) == 3)
	#print mean([2,4])
def test_float_mean():
	assert(mean([1,2])) == 1.5)

test_mean()
test_float_mean()