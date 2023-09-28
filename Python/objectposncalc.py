#Object Position Calculation

print("Welcome to Object Position Calculator!\n")
start = float(input("Please enter a starting position as a floating point value in meters: "))
#this is the starting position variable.
init_vel = float(input("Please enter an initial velocity in meters/second: "))
#this is the initial velocity value
accel = float(input("Please enter an acceleration value in meters/second/second: "))
#this is the acceleration value
t = float(input("And finally, please enter the time of travel for the object in seconds: "))
#this is time value
final_pos = start + (init_vel * t) + (0.5 * accel * (t ** 2)) #final position formula!!
print("The final position of the object is", final_pos)
