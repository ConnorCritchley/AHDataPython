# Connor Critchley Lab 3

num = int(input("Enter an integer"))  # primary input
flag = True  # loop flag
square = 0  # squared value
cube = 0  # cubed value

# Main loop
while flag:
    print(f"{'Number':<6} {'Squared':<6} {'Cubed':<}")  # print table header
    print("-" * 20)  # print table line
    for i in range(num):  # go through numbers up to num
        i += 1  # I LOVE OFF BY ONE ERRORS
        squared = i * i
        cubed = i * i * i
        print(f"{i :<6} {squared :<7} {cubed :<}")  # print table row
    if input("Continue? y/n") == 'y':  # check to continue and re-input
        num = int(input("Enter an integer"))
    else:  # otherwise end loop
        flag = False

# Attempting mult table very crudely, don't try with high numbers
header = "     "
equals = "     "
for i in range(num):
    i += 1
    header += f"{i:>4}"
    equals += f"{'=':>4}"
print(header)
print(equals)
row = ""
for i in range(num):
    i += 1
    row += f"{i:>3} |"
    for j in range(num):
        j += 1
        row += f"{(i * j):>4}"
    print(row)
    row = ""
