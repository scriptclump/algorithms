def matrixTranspose(x):
	result = [[0,0,0],
			 [0,0,0]]
	for i in range(len(x)):
		for j in range( len(x[0]) ):
			result[j][i] = x[i][j]
	
	print(result)


x = [[1,2],
	[4,5],
	[7,8]]
matrixTranspose(x)