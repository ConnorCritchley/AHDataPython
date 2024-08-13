# Lab 4
# Connor Critchley

def heating_cooling(actual_temp, desired_temp):
    print(f"Current temp: {actual_temp}\nDesired temp: {desired_temp}")
    if actual_temp < desired_temp:
        print("Run heat\n")
    elif actual_temp > desired_temp:
        print("Run A/C\n")
    else:
        print("Standby\n")


heating_cooling(60, 70)

heating_cooling(68, 65)

heating_cooling(int(input("Enter current temp: ")), int(input("Enter desired temp: ")))

# Extra challenge function. Unable to use switch(match) statements in this python version.
def convert_temp(temp_c, target_unit):
    if target_unit.upper() == 'C':
        print(temp_c)
    elif target_unit.upper() == 'F':
        print("F:", temp_c* (9/5) + 32)
    elif target_unit.upper() == 'K':
        print("K:", temp_c + 273.15)

convert_temp(30, 'F')
convert_temp(26, 'K')