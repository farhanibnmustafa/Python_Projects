def add(n1,n2):
    return n1+ n2

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1/n2

symbol_dictionary = {
   # In the given code snippet, ` '+' : 'add',` is creating a key-value pair in a dictionary called
   # `symbol_dictionary`.
    '+' : add,
    '-' : sub,
    '*' : mul,
    '/' : div
    
}
# TODO: give prompt to input first number
num1 = int(input("\n\n\nWhat's the first number?: "))

for symbol in symbol_dictionary:
    print(symbol)
want_operation = input("\nPick an operation of line above : ")
num2 = int(input("\nwhat's the second number?: "))
# if want_operation == '+':
    # print(num1, "+", num2, "=", add(num1,num2))
# elif want_operation == '-':
    # print(num1, "-", num2, "=", sub(num1,num2))
# elif want_operation == '*':
    # print(num1, "*", num2, "=", mul(num1,num2))
# elif want_operation == '/':
    # print(num1, "/", num2, "=", div(num1,num2))
# 
calculation_function = symbol_dictionary[want_operation]
answer1 = calculation_function(num1,num2)
print(f"\n\n{num1} {want_operation} {num2} = {answer1}")
want_operation =input("pick another operation : ")
num3 = int(input("What's the 3rd number? : "))
calculation_function = symbol_dictionary[want_operation]
answer2 = calculation_function(answer1, num3)
print(f"{answer1} {want_operation} {num3} = {answer2}")