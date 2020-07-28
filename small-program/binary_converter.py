def binaryConverter(num):
	print("The decimal value of", num, "is:")
	print("Binary = ", bin(num))
	print("Octal =", oct(num))
	print("Hexadecimal =", hex(num))

def asciiConverter(val):
	print("Hexadecimal =", ord(val))
	



binaryConverter(10)
asciiConverter('A')
