import random
from vslogo import vs_logo
from logo import logo
import os
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
data = [
    {"name": "John", 
     "followers": 1000, 
     "description": "Software Engineer", 
     "country": "USA"},
    {"name": " Alice", 
     "followers": 500, 
     "description": "Data Scientist", 
     "country": "Canada"},
    {"name": "Bob", 
     "followers": 2000, 
     "description": "AI Researcher", 
     "country": "UK"},
    {"name": "Eve", 
     "followers": 1500, 
     "description": "Machine Learning Engineer", 
     "country": "Australia"},
    {"name": "Charlie", 
     "followers": 800, 
     "description": "Full Stack Developer", 
     "country": "Germany"}
]
def check_result(select,a_followers,b_followers):
    if a_followers>b_followers:
        return select == "a"
    else:
        return select =="b"
        # if select == "a":
            # return True
        # else:
            # return False

score = 0
person_b = random.choice(data)
should_game_continue = True
print(logo)
while should_game_continue:
    person_a = person_b
    person_b = random.choice(data)
    while person_a == person_b:
        person_b = random.choice(data)
    # def first_detail():
        # print(name)
        # if description[0]== 'a' or 'i' or 'o' or 'u' or 'e':
            # print (f", an {description}")
        # else:
            # print(f", a {description}")
        # print(f"from {"country"}")
    # first_detail()
    a_followers_count = person_a["followers"]
    b_followers_count = person_b["followers"]
    print(f"\nCompare A : {person_a["name"]}, a {person_a["description"]}, from {person_a["country"]}\n")
    print(vs_logo)
    print(f"\nAgainst B : {person_b["name"]}, a {person_b["description"]}, from {person_b["country"]}")
    select = input("\nWho has more followers? Type 'A' or 'B' : ").lower()
    result = check_result(select,a_followers_count,b_followers_count)
    clear_console()
    print(logo)
    if result == True:
        score+=1
        print(f"\n\nYou are right! Your current score is {score}")
    else: 
        should_game_continue = False
        print(f"\n\nSorry that's wrong! Final score is {score}")
        