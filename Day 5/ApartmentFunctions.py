# Connor Critchley
# lab 5

# basic function
def apt_search1(city, max_rent, min_beds, pets_allowed):
    message = (f"Welcome to GC property management! Looking up listing in {str(city)} for {int(min_beds)} "
               "bedroom apartments")
    if pets_allowed:
        message += " that allow pets"
    message += f", all within a budget of ${max_rent} per month..."
    print(message)


# calls to basic to ensure both cases work
apt_search1("Dimmsdale", 1750, 2, True)
apt_search1("Hell, Michigan", 5750, 5, False)


# function with default values
def apt_search2(city, max_rent, min_beds=1, pets_allowed=False):
    message = (f"Welcome to GC property management! Looking up listing in {str(city)} for {int(min_beds)} "
               "bedroom apartments")
    if pets_allowed:
        message += " that allow pets"
    message += f", all within a budget of ${max_rent} per month..."
    print(message)


# Calls of new function
apt_search2("Dimmsdale", 1750)  # omit default values
apt_search2("Dimmsdale", 1750, 2)  # only omit pets
apt_search2("Dimmsdale", 1750, pets_allowed=True)  # only omit beds

# lambda function block
plus_one_hundred = lambda x : x + 100
square_num = lambda x : x * x
concatenate = lambda s : "- " + s
divide_by_three = lambda x : x / 3

print(plus_one_hundred(30))
print(square_num(4))
print(concatenate('hello'))
print(divide_by_three(9))
