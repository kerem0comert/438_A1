import re

def encrypt(): pass
def decrypt(): pass

def getTable():
    table = []
    with open("table.txt") as f:
        for row in [x.strip() for x in f.readlines()]: 
            """if a line contains any upper case letters at all, take anything 
            that is between singlequotes"""
            if any(x.isupper() for x in row): 
                table.append(re.findall(r"'(.*?)'", row))
    print(table)



def menu():
    print("Simple Cypher:")
    print("[1] Encrypt")
    print("[2] Decrypt")
    print("[3] Exit")
    selection = int(input("Select: "))
    if selection == 1: encrypt()
    elif selection == 2: decrypt()
    elif selection == 3: exit()
    else:
        print("Undefined selection!")
        menu()
        
if __name__ == "__main__":
    table = getTable()
    #menu()