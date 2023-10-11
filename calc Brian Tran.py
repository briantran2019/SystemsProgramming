import math
sum = 0.0 #float to store calculations

def n1check(): #prompts users continually until a vaild number is entered
    while True:
        n1 = input("Enter a number: ")
        if n1.isdigit():
            break
        else:
            print("Try again.")
    return n1
def n2check(): #same as n1
    while True:
        n2 = input("Enter a number: ")
        if n2.isdigit():
            break
        else:
            print("Try again.")
    return n2
def opcheck(): #prompts users to enter a supported operation, can be easily expanded by adding more strings to the vaild operatons array
    while True:
        op = input("Enter an operation to perform. +, -, *, /, ^, sqrt, log: ")
        if op in ['+', '-', '*', '/', '^', 'sqrt', 'log']:
            break
        else:
            print("Try again.")
    return op

n1 = n1check() #call input check functions
n2 = n2check()
op = opcheck()

while True: #main calculation loop using pythons version of a switch case. Also continually runs until the user wants to quit
    match op:
        case '+':
            print(str(n1) + " + " + str(n2) + " = " + str(int(n1) + int(n2)))
        case '-':
            print(str(n1) + " - " + str(n2) + " = " + str(int(n1) - int(n2)))
        case '*':
            print(str(n1) + " * " + str(n2) + " = " + str(int(n1) * int(n2)))
        case '/':
            print(str(n1) + " / " + str(n2) + " = " + str(int(n1) / int(n2)))
        case '^':
            print(str(n1) + " ^ " + str(n2) + " = " + str(int(n1) ** int(n2)))
        case 'sqrt':
            print("The square root of " + str(n1) + " is " + str(math.sqrt(int(n1))))
            print("The square root of " + str(n2) + " is " + str(math.sqrt(int(n2))))
        case 'log':
            print("The log of " + str(n1) + " using base " + str(n2) + " = " + str(math.log(int(n1), int(n2))))
    q = input("Would you like to quit? y/n: ") 
    if q == 'y': #check if the user wants to quit y
        print("Goodbye")
        break
    n1 = n1check() #call input check functions for new values because if the user wanted to quit, this code would not be reached
    n2 = n2check() 
    op = opcheck()