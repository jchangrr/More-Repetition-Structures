"""
Assignment #5, Problem #3b
Justyn Chang
"""
#calculate all prime numbers between 1 and 1000
num = 0
while True:
    num += 1
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
        if remainder == 0:
            break
        if count == num - 1:
            print(num, "is a prime number!")
            break
    if num == 1000:
        break

