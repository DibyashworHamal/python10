num = int(input("Enter a number:"))
sum = 0
temp = num
while num > 0:
    rem = num % 10
    sum = sum + rem
    num = num // 10
print("The sum of digit of", temp, "is:", sum)
