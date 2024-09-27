# Rock wins against scissors 
# paper wins against rock 
# and scissors wins against paper.
import random

rock = ''' 
                                      _______
                                  ---'   ____)
                                        (_____)
                                        (_____)
                                        (____)
                                  ---.__(___) '''

paper = ''' 
                                       _______
                                   ---'   ____)____
                                             ______)
                                             _______)
                                            _______)
                                   ---.__________)  '''

scissors = '''
                                       _______
                                   ---'   ____)____
                                             ______)
                                          __________)
                                         (____)
                                   ---.__(___) '''

while True:
    choose = input("\n\n\n\n\n\nWhat do you choose? Type '0' for Rock, '1' for paper or '2' for scissors.\n\n\n --> ")
    if choose not in ['0', '1', '2']:
        print("\n\nInvalid choice. Please choose a number between 0 to 2. ")
    else:
        choose = int(choose)
        if choose == 0:
            print(rock)
        elif choose == 1:
            print(paper)
        elif choose == 2:
            print(scissors)

        computer_choose = random.randint(0,2)
        print("\n\n\n\nComputer choose:\n\n")
        if computer_choose == 0:
            print(rock)
        elif computer_choose == 1:
            print(paper)
        else:
            print(scissors)

        if choose == computer_choose:
            print("It's a draw!")
        elif (choose == 0 and computer_choose == 2) or (choose == 1 and computer_choose == 0) or (choose == 2 and computer_choose == 1):
            print("\n\n\n\n                                    You win!")
        else:          
            print("\n\n\n\n                                    You lose!")