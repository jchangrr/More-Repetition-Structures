"""
Assignment #5, Problem #3d
Justyn Chang
"""
#ask for start and end numbers
start = int(input("Start number: "))
endn = int(input("End number: "))
#validate range
while True:
    if start <=0 or endn <= 0:
        print("Start and end must be positive")
        print()
        start = int(input("Start number: "))
        endn = int(input("End number: "))
    else:
        break
while True:
    if endn <= start:
        print("End number must be greater than start number")
        print()
        start = int(input("Start number: "))
        endn = int(input("End number: "))
    else:
        break

#find all prime numbers within range and align them in 10 columns
num = start - 1
column = 0
while True:
    num += 1
    count = 1
    while True:
        count += 1
        remainder = num % count
        if num == 1:
            break
        if num == 2:
            column += 1
            fnum = format(str(num), ">5s")
            print(fnum, end = "")
            break
        if remainder == 0:
            break
        if count == num - 1:
            column += 1
            if column % 10 == 0:
                fnum = format(str(num), ">5s")
                print(fnum)
            else:
                fnum = format(str(num), ">5s")
                print(fnum, end = "")
            break
    if num == endn:
        break

