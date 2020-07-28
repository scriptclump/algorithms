def fibonacci(num):
	fno = 0
	sno = 1
	tno = fno + sno
	series = [fno, sno]
	for i in range(num):
		tno = fno + sno
		fno = sno
		sno = tno
		series.append(tno)
	print(series)


fibonacci(10)