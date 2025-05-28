def main(my_list):
    data=input("Enter Some data to copy :")
    for i in range(3):
        my_list.append(data)
    print(my_list)
    
    
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main([])