def power(num):
	# use anonymous function
	result = list(map(lambda x: 2 ** x, range(num)))

	print("The total num are:",num)
	for i in range(num):
	   print("2 raised to power",i,"is",result[i])

power(10)