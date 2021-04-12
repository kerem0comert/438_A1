import re

def encrypt(plaintext, key): 
    
    #remove whitespace chars
    plaintext = re.sub(r"\s+", "", plaintext)
    print(plaintext)
    
def decrypt(cipher, key): pass

def getTable():
    table = []
    with open("table.txt") as f:
        for row in [x.strip() for x in f.readlines()]: 
            """if a line contains any upper case letters at all, take anything 
            that is between singlequotes"""
            if any(x.isupper() for x in row): 
                table.append(re.findall(r"'(.*?)'", row))
    return table


def getInputs():
    inputText = input("Inputtext: ")
    key = input("Key: ")
    return inputText, key


def menu():
    print("Simple Cypher:")
    print("[1] Encrypt")
    print("[2] Decrypt")
    print("[3] Exit")
    selection = int(input("Select: "))
    if selection == 1: 
        plaintext, key = getInputs()
        encrypt(plaintext, key)
    elif selection == 2: 
        cipher, key = getInputs()
        decrypt(cipher, key)
    elif selection == 3: exit()
    else:
        print("Undefined selection!")
        menu()
        
if __name__ == "__main__":
    table = getTable()
    menu()