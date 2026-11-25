# Program to print multiples of 5 from 50 down to 5

print("Multiples of 5 in reverse:")

# start = 50
# stop  = 0   (Python stops at 0 + 1 = 1, so 5 is included)
# step  = -5  (Subtracts 5 in each iteration)
for i in range(50, 0, -5):
    print(i, end=" ")