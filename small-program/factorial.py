def factorial(num):
	if(num < 0):
		print('factorial not exists for negetive number')
	elif(num == 0 or num == 1):
		print('Factorial of zero & one is 1 only')
	else:
		factorial = 1
		for i in range(1, num+1):
			factorial = factorial*i
		print("The factorial of",num,"is",factorial)

factorial(5)