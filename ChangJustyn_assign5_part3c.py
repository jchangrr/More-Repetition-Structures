"""
Assignment #5, Problem #3c
Justyn Chang
"""
#ask for start and end number
start = int(input("Start number: "))
end = int(input("End number: "))
#validate range
while True:
    if start <=0 or end <= 0:
        print("Start and end must be positive")
        print()
        start = int(input("Start number: "))
        end = int(input("End number: "))
    else:
        break
while True:
    if end <= start:
        print("End number must be greater than start number")
        print()
        start = int(input("Start number: "))
        end = int(input("End number: "))
    else:
        break
print()
#find all prime numbers between range
num = start - 1
while True:
    num += 1
    count = 1
    while True:
        count += 1
        remainder = num % count
        if num == 1:
            break
        if num == 2:
            print(num)
            break
        if remainder == 0:
            break
        if count == num - 1:
            print(num)
            break
    if num == end:
        break

