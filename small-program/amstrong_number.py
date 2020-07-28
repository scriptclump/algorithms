def amstrong_number(num):
	total = 0
	temp = num
	while temp > 0:
		digit = temp % 10
		total += digit ** 3
		temp //=10

	# display the result
	if num == total:
	   print(num,"is an Armstrong number")
	else:
	   print(num,"is not an Armstrong number")

amstrong_number(370)