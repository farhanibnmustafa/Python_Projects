# Instructions
# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1
# Example Input
# size = "L"
# add_pepperoni = "y"
# extra_cheese = "N"
# Example Output
# Your final bill is: $28.
print("                     \n\nWelcome to Pizza Deliveries!\n\n")
size = input("\nWhat size pizza wanna order?(S/M/L): ")
if size =="s":
    bill = 15
    print(f"\nYour bill is ${bill}")
elif size == "m":
    bill = 20
    print(f"\nYour bill is ${bill}")
else:
    bill = 25
    print(f"\nYour bill is ${bill}")
want_pepperoni = input("\nDo you want Pepperoni(y/n): ")
if want_pepperoni == "y":
    if size =="s":
        bill+= 2
        print(f"\n\nTotal bill ${bill}")
    elif size =="m" or size =="l":
        bill+= 3
        print(f"\n\nTotal bill ${bill}")
want_cheese = input("\nDo you want extra cheese(y/n): ")
if want_cheese == "y":
    bill+=1
    print(f"\n\nYour final bill is: ${bill}")
else:
    print(f"\n\nYour final bill is: ${bill}")
    print("\n\n\n")