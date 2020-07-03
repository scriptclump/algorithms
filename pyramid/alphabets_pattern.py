# Output

# A 
# B B 
# C C C 
# D D D D 
# E E E E E 
# F F F F F F 
# G G G G G G G 


n = 7
ascii = 65
for i in range(n):
	for j in range(i+1):
		print(chr(ascii), end=" ")
	ascii = ascii + 1
	print("\r")
