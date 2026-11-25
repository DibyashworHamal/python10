# Program to print Number, Square, and Cube from 1 to N

n = int(input("Enter limit N: "))

# Print table header
print("\nNumber\t| Square\t| Cube")
print("-" * 32)  # Prints 32 dashes as a divider line

# Loop runs from 1 to n (remember: range stops at n + 1)
for i in range(1, n + 1):
    square = i ** 2
    cube = i ** 3
    print(i, "\t|", square, "\t\t|", cube)