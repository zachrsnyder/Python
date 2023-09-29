import random

while True:
    try:
        values_num = int(input("How many random numbers do you want? "))
        if(values_num <= 0):
            print("Please enter a number greater than zero.\n")
            continue
    except ValueError:
        print("Please enter your answer as an integer value.\n")
    else:
        break
while True:
    try:
        value_min = int(input("What is the minimum for the random numbers? "))
    except ValueError:
        print("Please enter your answer as a integer value")
    else:
        break
while True:
    try:
        value_max = int(input("What is the maximum for the random numbers? "))
    except ValueError:
        print("Please enter your answer as a integer value")
    else:
        break
f = open("randomnum.txt", "w")
for x in range(0,values_num):
    f.write(f"{str(random.randrange(value_min,value_max+1))}\n")

print("Your random numbers have been written to the file \"randomnum.txt\"!\n")


