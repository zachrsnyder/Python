#Object Position Calculation

print("Welcome to Object Position Calculator!\n")
while(True):
    #acquire starting point
    while(True):
        try:
            start = float(input("Please enter a starting position as a floating point value in meters: "))
        except ValueError:
            print("Invalid entry. Please enter just a numerical value.\n")
            continue
        else:
            print("Thank You!\n")
            break
    #acquire initial velocity
    while(True):
        try:
            init_vel = float(input("Please enter an initial velocity in meters/second: "))
        except ValueError:
            print("Invalid entry. Please enter an initial velocity without units as a numerical value.\n")
            continue
        else:
            print("Thank You!\n")
            break
    #this is the acceleration value
    while(True):
        try:
            accel = float(input("Please enter an acceleration value in meters/second/second: "))
        except ValueError:
            print("Invalid Entry. Please enter an acceleration value without units\n")
            continue
        else:
            print("Thank You!\n")
            break
    #acquire positive time value
    while(True):
        try:
            t = float(input("And finally, please enter the time of travel for the object in seconds (time must be a positive value): "))
            if(t < 0):
                print("Time must be positive. Please try again.\n")
                continue
        except ValueError:
            print("Invalid Entry. Time must be entered as a decimal value without units.\n")
            continue
        else:
            print("Thank You!\n")
            break
    final_pos = start + (init_vel * t) + (0.5 * accel * (t ** 2)) #final position formula!!
    print("The final position of the object is", final_pos,"\n")
    flag = input("Would you like to make another calculation? (y/n): ")
    #asking if they wish to continue
    if(flag != "y"):
        print("Thank you for using Object Position Calculator!\n")
        break



