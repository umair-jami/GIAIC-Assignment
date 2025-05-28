list1=[1,2,3,4,5,6,7,8,9]
def main(num_list):
    """Double the value of each list item"""
    updated_list=[]
    for num in num_list:
        double_num=num+num
        updated_list.append(double_num)
    print(updated_list)
        



# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main(list1)