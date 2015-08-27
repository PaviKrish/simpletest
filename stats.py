def mean(vals):
	total = float(sum((vals)))
	lenght = len(vals)
	return total/lenght 
def std(vals):
	n = len(vals) 
	if n == 0:
		return 0.0
	mu = mean(vals) 
	var =0.0 
	for val in vals:
		var = var + (val-mu)**2
	return (var/n)**0.5 
	
	
	
#def test_mean():
#	assert(mean([2,4]) == 3)
#	#print mean([2,4])
#def test_float_mean():
#	assert(mean([1,2])) == 1.5)

#test_mean()
#test_float_mean()
