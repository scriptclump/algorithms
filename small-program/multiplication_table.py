def multiplicationTable(num):
	if(num > 0):
		for i in range(1, 11):
			table = num * i
			print(num, i, table)


multiplicationTable(13)