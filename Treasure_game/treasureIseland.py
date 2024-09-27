print(r'''
                                     _                                     _     _                 _ 
                               | |                                   (_)   | |               | |
                               | |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
                               | __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
                               | |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
                                \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                
                                ''')
print('''
                         *******************************************************************************
                                   |                   |                  |                     |
                          _________|________________.=""_;=.______________|_____________________|_______
                         |                   |  ,-"_,=""     `"=.|                  |
                         |___________________|__"=._o`"-._        `"=.______________|___________________
                                   |                `"=._o`"=._      _`"=._                     |
                          _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
                         |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
                         |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                                   |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
                          _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
                         |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
                         |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
                         ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
                         /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
                         ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
                         /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
                         ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
                         /______/______/______/______/______/______/______/______/______/______/______/_
                         *******************************************************************************
                        
                        
                        
                         ''')
print("                                                  Welcome to Treasure Island!\n                                          Your mission is to find the hidden treasure.\n\n")
choice1 = input("                             You're at a crossroad, where do you want to go? Type 'left or 'right'.\n\n                            \t\t\t   --> ").lower()
if choice1 == "left":              
    choice2 = input("                  \nYou come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat or Type 'swim' to swim across.\n\n      \t\t\t\t\t\t --> ").lower()
    if choice2 == "wait":
        choice3 =input("                                    \n\t\tYou arrive at the island unharmed. There is a house with 3 doors (Red, Yellow, Blue) .\n\n                         \t\tWhich color do you choose?\n\n     \t\t\t\t\t\t--> ").lower()
        if choice3 == "red":
            print("               \n\t\t\t\t\t ******* It's a room full of fire. *******\n\n                        \t\t\t\t\t\t<----- Game Over ----->\n\n\n")
        elif choice3 == "yellow":
            print("                \n\t\t\t\t\t ******* You found the treasure! *******\n\n                    \t\t\t\t\t\t <----- Congratulations! You Win! ----->\n\n\n")
        elif choice3 == "blue":
            print("                \n\t\t\t\t******* You enter a room of beasts. *******\n\n                 \t\t\t   <----- Game Over ----->\n\n\n")
        else:
            print("             \n\t\t\t\t\t******* You chose a door that doesn't exist. *******\n\n               \t\t\t\t\t\t    <----- Game Over ----->\n\n\n")
    else:
        print("                 \n\t\t\t\t\t ******* You got attacked by an angry trout. *******\n\n         \t\t\t\t\t\t\t      <----- Game Over ----->\n\n\n")       
else:   
    print("                      \n\t\t\t\t      ******* You fell in a hole. ******* \n\n              \t\t\t           <----- Game Over ----->\n\n\n") 