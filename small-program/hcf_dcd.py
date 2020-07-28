def hcf(x,y):
	sm_val = x
	if( x > y):
		sm_val = y
	else:
		sm_val = x

	for i in range(1, sm_val+1):
		if( (x % i == 0) and (y % i) == 0):
			hcf = i

	return hcf

val = hcf(54, 24)
print(val)

