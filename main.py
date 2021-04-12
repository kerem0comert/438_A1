def encrypt(): pass
def decrypt(): pass


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
    menu()