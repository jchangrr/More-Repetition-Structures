"""
Assignment #5, Problem #3a
Justyn Chang
"""
#ask for positive number
num = int(input("Enter a positive number to test: "))
#validate number
while True:
    if num <= 0:
        print("Invalid number, try again.")
        num = int(input("Enter a positive number to test: "))
    else:
        break
print()

#calculate if number is prime or not
count = 1
while True:
    count += 1
    remainder = num % count
    if num == 1:
        print(num, "is technically not a prime number.")
        break
    if num == 2:
        print(num, "is a prime number!")
        break
    if remainder != 0:
        print(count, "is NOT a divisor of", num, " ... continuing")
    elif remainder == 0:
        print(count, "is a divisor of", num, " ... stopping")
        print()
        print(num, "is not a prime number.")
        break
    if count == num - 1:
        print()
        print(num, "is a prime number!")
        break
