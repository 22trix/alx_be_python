length = int(input("Enter the size of the pattern: "))

row = 0
while row < length:
    for col in range(length):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1