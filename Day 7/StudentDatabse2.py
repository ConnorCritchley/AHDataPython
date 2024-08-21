# day 7 lab assignment
# Connor Critchley

data = [  # primary data/dictionary list
  {"name": "Tina", "hometown": "Portland", "favorite_food": "puppy chow"},
  {"name": "Klaus", "hometown": "Frankfurt", "favorite_food": "pizza"},
  {"name": "Julia", "hometown": "Houston", "favorite_food": "shrimp"}
]
running = True  # main loop flag


# Function that lists all names in the main data list
def list_names(list):
    i = 1
    for student in list:
        print(f"{i}. {student['name']}")
        i += 1


# Returns if action input is valid option
def a_validate(action):
    return action.upper() in "ADD" or action.upper() in "VIEW" or action.upper() in "QUIT"


# returns is index input is valid option
def i_validate(index):
    return 0 < (index + 1) <= len(data)


# returns is category input is valid option
def c_validate(category):
    return (category.upper() in "HOMETOWN") or (category.upper() in "FAVORITE FOOD")


# Creates a new student dictionary and appends to main data list
def get_new_student():
    student = {"name": input("What is the student's name?\n"),
               "hometown": input("What is the student's hometown?\n"),
               "favorite_food": input("What is the student's favorite foodvir?\n")}
    data.append(student)


# main loop
while running:
    # Start with action prompt, then validate it
    action = input("Select your action: add, view, or quit.\n")
    while not a_validate(action):
        action = input("Invalid. Actions are 'add', 'view', or 'quit'.\n")

    # run through possible action cases
    if action.upper() in "QUIT":  # if quit, end loop
        running = False

    # Else if view, list names and let them select info
    elif action.upper() in "VIEW":
        list_names(data)
        i = int(input(f"Select a student, enter 1-{len(data)}\n")) - 1
        while not i_validate(i):
            i = int(input(f"Invalid, enter 1-{len(data)}\n")) - 1
        category = input(f"Student {i + 1} is {data[i]['name']}. Enter 'hometown' or 'favorite food'.\n")
        while not c_validate(category):  # while not valid, loop input
            category = input("Invalid. Enter either 'hometown' or 'favorite food'\n")
        if category.upper() in "HOMETOWN":  # if input is hometown, display
            print(f"{data[i]['name']} is from {data[i]['hometown']}.")
        else:  # else it must be favorite food
            print(f"{data[i]['name']}'s favorite food is {data[i]['favorite_food']}.")

    #  since already validated, final action case must be add
    else:
        get_new_student()  # call addition function
