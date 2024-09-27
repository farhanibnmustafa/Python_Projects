############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import os
import random
from LogoBlackJack import logo
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def deal_card():
    """Return a random card from the deck."""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. 
# If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0),
# then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. 
# If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "\n\n\nIt's a draw!😒"
    elif computer_score == 0:
        return "\n\n\nYou lose! Opponent has a BlackJack.😥"
    elif user_score == 0:
        return "\n\n\nYou win with a BlackJack!🤩"
    elif user_score>21:
        return "\n\n\nYou went over. You lose!😔"
    elif computer_score>21:
        return "\n\n\nOpponent went over. You win!😃"
    elif computer_score>user_score:
        return "\n\n\nYou lose! Opponent has a higher score.☹️"
    else:
        return "\n\n\nYou win! You have a higher score.🥳"
    
    
#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards):
    
    """calculate the score of a hand of cards"""
    return sum(cards)
    #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards)==2:
        return 0
    #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)

def playGame():
    print("\n\n\n\n\n\n\n")
    print(logo)
    #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []
    
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    is_game_over = False
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" \n\nYour cards {user_cards}, Current score {user_score}\n")
        print(f" \nComputer's first card {computer_cards[0]}\n")
        if user_score == 0 or computer_score==0 or user_score>21:
            is_game_over  = True
        #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
        else:
            user_deal_card = input("\n\n\n\nType 'y' for drawing another card or type 'n' to pass: ").lower()
            if user_deal_card == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
        #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    
    #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"\n\nYour final hand {user_cards}, Final score {user_score}")
    print(f"\n\nDealer's final hand {computer_cards}, Final score {computer_score}")
    print(compare(user_score, computer_score))
#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of 
# blackjack and show the logo from art.py.
while (input("\n\n\n\n\n\nDo you want play BlackJack game? Type 'y' or 'n': ").lower())== 'y':
    clear_console()
    playGame()

