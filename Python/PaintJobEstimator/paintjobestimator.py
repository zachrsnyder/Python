#Paint Company Appraisal
#Zach Snyder
#Python 1
#Sept. 17th, 2023

import math

print("Welcome to Paint Job Estimator!\n")

while(True):
    while(True):
        #acquire square footage as a non-negative decimal value
        try:
            sqFt = float(input("Please Enter the Square Feet of wall to be painted: "))
            if(sqFt < 0):
                print("Please enter a non-negative value as you square feet of wall.\n")
                continue
        except ValueError:
            print("Please enter a decimal value representing the square footage of wall to be painted. No units are required in your answer.\n")
        else:
            break
    while(True):
        #acquire paint cost as a non-negative decimal value
        try:
            paint = float(input("Please enter the cost of your desired paint per gallon: "))
            if(paint < 0):
                print("Please enter a non-negative value as the cost of paint per gallon.\n")
                continue
        except ValueError:
            print("Please enter your answer as a decimal value representing the cost of your paint per gallon.\n")
        else:
            break
    #Calculating all of the values to be displayed to the user
    gallons = math.ceil(sqFt/350) #rounds up to integer value
    paintPrice = paint * gallons 
    laborHrs = 6 * sqFt/350
    laborCost = laborHrs * 62.25
    total = laborCost + paintPrice
    print("\nThis job requires ", gallons," gallons of paint.\n")
    print("It is estimated to take ", round(laborHrs, 1)," hours to complete.\n")
    print("The paint is to cost $", round(paintPrice, 2),"\n")
    print("The labor cost is $", round(laborCost, 2),"\n")
    print("The total cost of this job is: $",round(total, 2),"\n")
    again = input("Would you like to do another estimate? (y/n)")
    #Offers another calculation. If not, program terminates
    if(again != "y"):
        print("Thank you for using the Paint Job Estimator!\n")
        break








    




