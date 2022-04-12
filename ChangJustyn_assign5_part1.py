"""
Assignment #5, Problem #1
Justyn Chang
"""
#ask for inputs for budget, slice and pie cost, and people attending
budget = float(input("Enter budget for your party: "))
slice_cost = float(input("Cost per slice of pizza: "))
pie_cost = float(input("Cost per whole pizza pie (8 slices): "))
party = int(input("How many people will be attending your party? "))

#ask number of slices per person
person = 0
total_slices = 0
while True:
    person += 1
    print("Enter number of slices for person #", person, sep = "", end = "")
    slices = int(input(": "))
    while True:
        if slices < 0:
            #validate slice #
            print("Not a valid entry, try again!")
            print()
            print("Enter number of slices for person #", person, sep = "", end = "")
            slices = int(input(": "))
        else:
            break
    total_slices = total_slices + slices
    if person == party:
        break

#calculate amount of pies and slices needed to buy
pies_final = total_slices // 8
slices_final = total_slices % 8

#calculate cost
cost = (pies_final * pie_cost) + (slices_final * slice_cost)
fcost = format(float(cost), ".2f")
cost = float(cost)

#calculate leftover amount
leftover = format(float(budget - cost), ".2f")
fleftover = float(leftover)
#tell how many pizzas to buy if under budget
if fleftover > 0:
    print("You should purchase", pies_final, "pies and", slices_final, "slices")
    print("Your total cost will be:", fcost)
    print("You will still have", leftover, "left after your order")
#tell how many pizzas to buy if exactly at budget
elif fleftover == 0:
    print("You should purchase", pies_final, "pies and", slices_final, "slices")
    print("Your total cost will be:", fcost)
    print("You will have no money left after your order.")
#tell if cost goes over budget
else:
    over = format(float(fleftover * -1), ".2f")
    print("Your order cannot be completed.")
    print("You would need to purchase", pies_final, "pies and", slices_final, "slices")
    print("This would put you over budget by", over)
