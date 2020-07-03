# Output
#
# A 
# B C 
# D E F 
# G H I J 
# K L M N O 
# P Q R S T U 

n = 7
ascii = 65
for i in range(n):
	for j in range(i+1):
		print(chr(ascii), end=" ")
		ascii = ascii + 1
	print("\r")
