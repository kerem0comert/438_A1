import re
from string import ascii_lowercase
from itertools import cycle

table = []

def pos(letter): return ascii_lowercase.index(letter)

"""itertools' built-in cycle module can create a generator from a given string
to yield what is needed, until the length constraint is satisfied."""
def repeatKey(key, length):
    letterPool = cycle(key)
    while len(key) < length:
        key += next(letterPool)
    return key
    
    
def encrypt(plaintext, key): 
    print("**********Encryption**********")
    print("Encryption Phase-1")

    #remove whitespace chars
    plaintext = re.sub(r"\s+", "", plaintext)
    
    #make sure that the length of key can accomadate the plaintext
    if len(plaintext) > len(key): 
        key = repeatKey(key, len(plaintext))

    cipher = ""
    for index, _ in enumerate(plaintext):
        cipher += table[pos(key[index])][pos(plaintext[index])]
    print(f"Plaintext: {plaintext}\nKey: {key}\nOutput (phase-1): {cipher}\n")
    print("Encryption Phase-2")
    if len(cipher) % 2: cipher += '0'
    
    firstHalf, secondHalf = cipher[:len(cipher)//2], cipher[len(cipher)//2:]
    
    
    
def decrypt(cipher, key): pass

def createTable():
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
    print(ascii_lowercase)
    createTable()
    menu()