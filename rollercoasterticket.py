print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
if height>120:
    print("You can ride the rollercoaster!")
    age = int(input("Enter your age: "))
    if age<12:
        bill = 5
        print(f"Your ticket price is ${bill}")
    elif age>12 and age<18:
        bill = 7
        print(f"Your ticket price is ${bill}")
    else:
        bill = 12
        print(f"Your ticket price is ${bill}")   
else:
    print("Sorry, you have to grow taller before you can ride.")
photo=input("Do you want photos?(yes or no): ")
if photo =="yes":
    bill+= 3
    print(f"The total bill is {bill}")
else:
    print(f"The total bill is {bill}")