# Connor Critchley Lab 2

name = input("What's your name?")  # username input
num = int(input("Enter a number between 1-100"))  # get num from user
Lflag = True  # loop flag for validation loop
flag = True  # main loop flag

# main loop
while flag:
    # input validation loop
    while Lflag:
        if (num >= 1) & (num <= 100):  # check 1-100 inclusive
            Lflag = False  # Valid, end loop and move on
        else:
            num = int(input("Enter a number between 1-100"))  # else redo input and loop

    # output conditionals
    if num % 2 == 0:  # if even
        if (num >= 2) & (num <= 24):
            print(f"{name}, your number is even and less than 25")
        elif (num >= 26) & (num <= 60):
            print(f"{name}, your number is even and between 26 and 60 inclusive")
        else:
            print(f"{name}, your number is even and greater than 60")
    else:  # odd
        if num < 60:
            print(f"{name},your number is odd and less than 60")
        else:
            print(f"{name},your number is odd and greater than 60")
    if input("Go again? y/n") == "y":
        num = int(input("Enter a number between 1-100"))
    else:
        flag = False