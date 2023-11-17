
OperationList = ['+', '-', '*', '/']


# Create a welcome page with different options, like instructions, the Calculetor itself, and maybe an exit option.
# Create a "MainCalc" function to wrap everything in a function.
# Keeping in mind that in the future I will create a GUI, and im not sure how it works yet, but I guess different buttons will direct the user to different functions.



def CalcInput1():
    try:
        global userFirstNum
        userFirstNum = int(input("Choose the first number: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        CalcInput1()
    return userFirstNum

CalcInput1()


def CalcOperation():
    global userOperation
    userOperation = input("Choose an operation to make from: "+ ','.join(OperationList) + " : ")

    if userOperation not in OperationList:
        print("The operation you choose is not valid, please choose one of the operation in the list: "+','.join(OperationList) + " : ")
        CalcOperation()
    else:
        pass

CalcOperation()


def CalcInput2():
    try:
        global userSecondtNum
        userSecondtNum = int(input("Choose the second number: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        CalcInput2()
    return userSecondtNum

CalcInput2()

#  Tests: 
# print(userOperation)
# print(type(userOperation))

# define functions for each operation - Done.
# Basically I decied to make every input an function and each operation a function that can be called when needed.


# Operation functions:

sentance = "Your answer is: "

def addition(x,y):
    print(sentance, x+y)
    return x + y

def subtraction(x,y):
    print(sentance, x-y)
    return x - y

def multiplication(x,y):
    print(sentance, x*y)
    return x * y

def devision(x,y):
    print(sentance, x/y)
    return x / y


# Main logic for different operations

if userOperation == '+':
    addition(userFirstNum, userSecondtNum)
elif userOperation == '-':
    subtraction(userFirstNum, userSecondtNum)
elif userOperation == '*':
    multiplication(userFirstNum, userSecondtNum)
elif userOperation == '/':
    devision(userFirstNum, userSecondtNum)
else:
    print("The operation you choose is not from the list of operations. Please try again.")



