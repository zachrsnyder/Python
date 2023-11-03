
cipher = {
    "a": "0",
    "b": "1",
    "c": "2",
    "d": "3",
    "e": "4",
    "f": "5",
    "g": "6",
    "h": "7",
    "i": "8",
    "j": "9",
    "k": "!",
    "l": "@",
    "m": "#",
    "n": "$",
    "o": "%",
    "p": "^",
    "q": "&",
    "r": "*",
    "s": "(",
    "t": ")",
    "u": "-",
    "v": "+",
    "w": "<",
    "x": ">",
    "y": "?",
    "z": "=",
}

decode_list = list(cipher.keys())
encode_list = list(cipher.values())

def decision():
    while True:
        print("1. Encode a message\n2. Decode a message\n3. Exit\n")
        while True:
            try:
                x = int(input("What would you like to do? "))
                if(x != 1 and x != 2 and x != 3):
                    print("Please enter a number 1 through 3\n")
                    continue
            except ValueError as a:
                print(f"An {a} occurred\n")
            else:
                return x
            
def encode():
    woah = list(input("Enter a message to encode: "))
    for i in range(0,len(woah)):
        woah[i] = cipher[woah[i]]
    single_string = ''
    for j in woah:
        single_string += j
    print("Your encoded message is ",single_string)
    return

def decode():
    sheesh = input("Enter a message to decode: ")
    darnit = list(sheesh)
    for y in range(0, len(darnit)):
        position = encode_list.index(darnit[y])
        darnit[y] = decode_list[position]
    single_str = ''
    for h in darnit:
        single_str += h
    print(f"Your decoded message is {single_str}\n")
    return

    

def main():
    print("Welcome to the Secret Message Encoder/Decoder\n")
    while True:
        x = decision()
        if(x == 1):
            encode()
        if(x == 2):
            decode()
        if(x == 3):
            break

main()
        

        
            
    

                

    