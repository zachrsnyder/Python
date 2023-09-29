try:
    f = open("randomnum.txt", "r")
except FileNotFoundError:
    print("The file \"randomnum.txt\" could not be found.\n")
else:
    i = 0
    print("List of random numbers in randomnum.txt:\n")
    for x in f:
        print(x)
        i += 1
    print(f"There were {i} random numbers in \"randomnum.txt\".")
    f.close()
    


