# inessyway
import random
print("Welcome to PyPassword Generator!\n")
char_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number_list = ['0','1','2','3','4','5','6','7','8','9']
symbol_list = symbols = [
    "@",  # At
    "#",  # Number, hashtag
    "$",  # Dollar, currency
    "%",  # Percent
    "&",  # Ampersand
    "*",  # Asterisk
    "+",  # Plus
    "-",  # Minus, hyphen
    "=",  # Equal
    "/",  # Slash, divide
    "\\", # Backslash
    "!",  # Exclamation mark
    "?",  # Question mark
    "^",  # Caret, exponentiation
    "~",  # Tilde
    "<",  # Less than
    ">",  # Greater than
    "{}", # Curly braces
    "[]", # Square brackets
    "()", # Parentheses
    "|",  # Vertical bar, pipe
    "_",  # Underscore
    "\"", # Quotation marks
    "'",  # Apostrophe, single quote
    "`"   # Backtick
]
password_letter=int(input("How many letter would you like in your password? --> "))
password_symbols =  int(input("How many symbols would you like to have? --> "))
password_num = int(input("How many number would you like to have? -->"))

password = ""
for char in range(1, password_letter+1):
    password+= random.choice(char_list)
for symbol in range(1, password_symbols+1):
    password+= random.choice(symbol_list)
for number in range(1, password_num+1):
    password+= random.choice(number_list)

print(f"Your password would be {password}")


