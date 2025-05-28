def get_first_element(list2):
    """Print the first element of provided list"""
    print(list2[0])


def main():
    list1=[]
    list_input=input("Please Enter the element of the list with space :")
    list_element=list_input.split()
    for item in range(1,len(list_element)+1):
        list1.append(item)
    get_first_element(list1)
    print(list1)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()