

def main():
    my_list=[]
    val=input("Enter the list value or Press Enter to quit :")
    while val:
        my_list.append(val)
        val=input("Enter the list value or Press Enter to quit :")
    print(my_list)
    num_dict={}
    for item in my_list:
        if item in num_dict:
            num_dict[item]+=1
        else:
            num_dict[item]=1
    """Loop over dictionary and print out each key and its value"""
    for num in num_dict:
        print(str(num) + " appears " + str(num_dict[num]) + " times.")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()