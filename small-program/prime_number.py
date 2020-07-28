def primeNumber(num):
	if (num > 1):
		for i in range(2, num):
			if(num % i == 0):
				print('{0} is prime number'.format(num))
				break
		else:
			print('{0} is not a prime number'.format(num))


primeNumber(6)