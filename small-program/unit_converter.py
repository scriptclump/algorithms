def temperatureConverter(temp, unit = 'celsius'):
	if unit == 'celsius': 
		fahrenheit = (temp * 1.8) + 32
		print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(temp,fahrenheit))
	else:
		celsius = (temp - 32) / 1.8
		print('%0.1f degree Fahrenheit is equal to %0.1f degree Celsius' %(temp,fahrenheit))


def distanceConverter(distance, unit = 'kilometers'):
	conv_fac = 0.621371
	if(distance == 'kilometers'):
		miles = distance * conv_fac
		print('%0.2f kilometers is equal to %0.2f miles' %(distance,miles))
	else:
		kilometers = distance / conv_fac
		print('%0.2f miles is equal to %0.2f kilometers' %(distance,kilometers))



temperatureConverter(40)
distanceConverter(100)