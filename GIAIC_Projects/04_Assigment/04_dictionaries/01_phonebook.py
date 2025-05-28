def read_phone_number():
    """
    Ask the user for names/number
    """
    phonebook={}
    while True:
        name=input("Name :")
        if name == "":
            break
        number=input("Number :")
        phonebook[name]=number
    return phonebook

def print_phonebook(phonebook):
    """prints out all the names/numbers
    """
    for name in phonebook:
        print(str(name) + " "+ str(phonebook[name]))
def lookup_phone(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("Enter the name to find the numbers")
        if name == "":
            break   
        if name not in phonebook:
            print(name + "is not in the phonebook")
        else:
            print(phonebook[name])
    
def main():
    phonebook=read_phone_number()
    print_phonebook(phonebook)
    lookup_phone(phonebook)

if __name__ == "__main__":
    main()
        