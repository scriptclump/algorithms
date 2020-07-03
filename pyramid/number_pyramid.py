# Output
#
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

n = 10
for i in range(n):
	k = 1
	for j in range(i+1):
		print(k, end=" ")
		k = k + 1
	print("\r")
