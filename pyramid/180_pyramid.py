n = 5
# number of spaces
k = 2 * n - 2

# outer loop to handle number of rows
for i in range(n):

    # inner loop to handle number spaces
    # values changing acc. to requirement
    for j in range(k):
        print(end=" ")

        # decrementing k after each loop
    k = k - 2

    # inner loop to handle number of columns
    # values changing acc. to outer loop
    for m in range(i + 1):
        # printing stars
        print("* ", end="")

        # ending line after each row
    print("\r")
