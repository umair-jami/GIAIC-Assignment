list1=[1,2,3,4,5,6,7,8,9]
def main(num_list):
    """This function takes a list of numbers and returns the sum of all the numbers in the list."""
    total =0
    for num in num_list:
        total+=num
    print("Sum of all list number is ", total)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main(list1)