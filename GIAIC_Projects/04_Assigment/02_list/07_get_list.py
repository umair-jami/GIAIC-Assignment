def main():
    my_list=[]
    list_item=input("Enter the list element or Press Enter only to quite :")
    while list_item:
        my_list.append(list_item)
        list_item=input("Enter the list element or Press Enter only to quite :")
    print("Here's the list:", my_list)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()