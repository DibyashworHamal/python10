n = int(input("Enter a number: "))
# Print even numbers from 1 to 
print("Even numbers from 1 to", n, "are:")
for i in range(2, n + 1, 2):
    print(i, end=' ')

# print Odd numbers from 1 to n
print("\n\nOdd numbers from 1 to", n, "are:")
for i in range(1, n + 1, 2):
    print(i, end=' ')

# Counting down from n to 1
print("\n\nCounting down from", n, "to 1:")
for i in range(n, 0, -1):
    print(i, end=' ')