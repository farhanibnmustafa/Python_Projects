# Instructions from your teacher:
    
#     1     2     3
# 1 ['📦', '📦', '📦'] 

# 2 ['📦', '📦', '📦']

# 3 ['📦', '📦', '📦']

# Your program should allow you to enter the position of the treasure using a two-digit system. The first digit is the horizontal column number and the second digit is the vertical row number. e.g:
# Example Input 1:
# column 2, row 3 would be entered as:
# 23
# Example Output 1:
#     1     2     3
# 1 ['📦', '📦', '📦'] 

# 2 ['📦', '📦', '📦']

# 3 ['📦', '💰', '📦']

# row1 = ['📦', '📦', '📦']
# row2 = ['📦', '📦', '📦']
# row3 = ['📦', '📦', '📦']
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Enter the position of the treasure using a two-digit number which means the column and row number: ")
# horizontal = int(position[0])
# vertical = int(position[1])
# map[vertical-1][horizontal-1] = "💰"
# print(f"{row1}\n{row2}\n{row3}")
import random
row1 = ['📦', '📦', '📦']
row2 = ['📦', '📦', '📦']
row3 = ['📦', '📦', '📦']
map = [row1, row2, row3]

# Randomly place the treasure on the map
treasure_row = random.randint(0, 2)
treasure_col = random.randint(0, 2)
map[treasure_row][treasure_col] = '💰'

print(f"{row1}\n{row2}\n{row3}")

while True:
    position = input("Enter the position of the treasure using a two-digit number which means the column and row number: ")
    horizontal = int(position[0]) - 1
    vertical = int(position[1]) - 1

    if horizontal < 0 or horizontal > 2 or vertical < 0 or vertical > 2:
        print("Invalid input. Please enter a number between 1 and 3.")
    elif map[vertical][horizontal] == '💰':
        print(f"\n\n{row1}\n{row2}\n{row3}\n\nCongratulations! You found the treasure!")
        break
    else:
        print("Sorry, that's not the correct position. Try again!")