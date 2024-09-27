# Instructions
# You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
# Important: You are not allowed to use the choice () function.
# Don't worry about the lines 3/4 it's there to allow us to test your code.
# Line 8 splits the string namesAsCSV into individual names and puts them inside a List called names.
# Example Input
# Angela, Ben, Jenny, Michael, Chloe
# Example Output
# Michael is going to buy the meal today!
# e.g. When you hit run, this is what should happen:
import random
names =input("\n\nGive me all of your names seperated by ',': ")
nameList = names.split(",")
nameCount = len(nameList)
randomName = random.randint(0, nameCount-1)
who_will_pay = nameList[randomName].strip() #add strip function to avoid whitespaces
print("\n\n")
print(who_will_pay + " is going to buy the meal today!\n\n")
