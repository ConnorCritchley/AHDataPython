# Lab project 6
# Connor Critchley

# list/var initializing
names = ["Eric Nylund", "James Bosch", "Bartholomew Humfterkuffle", "Skimbledorf Blamsnaf", "Bob Bobson"]
hometowns = ["Baltimore", "Miami", "Bermuda", "the Mages' Guild", "Richmond"]
foods = ["Bourbon Salmon", "Key Lime Pie", "Caviar", "Wizard's Draught", "Mac n Cheese"]
loop = True


# Validation function, takes index and range to ensure index is within 0-range
def i_validate(index, ranged):
    return index in range(ranged)


# Validation for category, allowing varying cases and partial entries of input string
def c_validate(category):
    return (category.upper() in "HOMETOWN") or (category.upper() in "FAVORITE FOOD")


# main run loop
while loop:
    i = int(input(f"Welcome! Select a student id 1-{len(names)}\n")) - 1  # set user search index and correct off-by-one
    while not i_validate(i, len(names)):  # As long as validation fails, loops input
        i = int(input(f"Invalid id. Select a student id 1-{len(names)}\n")) - 1
    print(f"Student {i + 1} is {names[i]}. What would you like to know?")

    category = input("Enter 'Hometown' or 'Favorite Food'\n")  # set user search category
    while not c_validate(category):  # As long as validation fails, loops input
        category = input("That category doesn't exist. Enter 'Hometown' or 'Favorite Food'\n")
    if category.upper() in "HOMETOWN":
        print(f"{names[i]} is from {hometowns[i]}.")
    else:  # Already validated, check for hometown, else food
        print(f"{names[i]}'s favorite food is {foods[i]}.")

    # Check for end of main loop
    if input("Would you like to check another student? y/n\n") == 'n':
        loop = False
