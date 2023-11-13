OperationList = ['+', '-', '*', '/']
userFirstNum = int(input("Choose the first number: "))
userOperation = input("Choose an operation to make from: "+ ','.join(OperationList) + " : ")
userSecondtNum = int(input("Choose the second number: "))

print(userOperation)
print(type(userOperation))

# define functions for each operation,
# later can make an if else base on the input and then call the different functions.
# when creating if else aldo adress cases where input is not number and other cases like this.
# keep in mind when writing the code, later a GUI will be added so work in small components.



# Functions: 

# the functions are working, but im not sure if creating a function for each operation is the best way.
# for now I used the if statments, and if the GUI will require a function, I'll use those as well.


# def addition (x,y):
#     print("This is the addition function, the answer is: ", x+y)
#     return x + y

# def subtraction (x,y):
#     print("This is the subtraction operation, the answer is: ", x-y)
#     return x - y



# Accepting input, testing cases, and passing to a function: 

# cases to notify the user
# - when the / is the other way around - \ notify the user and rout to the devision option
# when any of the inputs are not numbers (a python error pops, need to find a way to handle such cases.)

sentance = "Your answer is: "

if userOperation == '+':
    # addition(userFirstNum, userSecondtNum) # addition function defined above.
    print(sentance, int(userFirstNum) + int(userSecondtNum))
elif userOperation == '-':
    # subtraction function
    print(sentance, int(userFirstNum) - int(userSecondtNum))
elif userOperation == '*':
    # multiplication funtion
    print(sentance, int(userFirstNum) * int(userSecondtNum))
elif userOperation == '/':
    # devision function
    print(sentance, int(userFirstNum) / int(userSecondtNum))
else:
    print("The operation you choose is not from the list of operations. Please try again.")
