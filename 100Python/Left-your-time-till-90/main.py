print("Welcome to the World! Wanna know how much time you left till 90?\n")
age = int(input("What is your current age?\n"))
years_remaining = 90 - age
months_remaining = years_remaining * 12
week_remaining = years_remaining * 52 #1 year = 52 weeeks
day_remaining = years_remaining * 365
print(f"\nYou have {day_remaining} days, {week_remaining} weeks, and {months_remaining} months left.")