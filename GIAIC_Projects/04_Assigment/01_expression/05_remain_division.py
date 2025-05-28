def main():
    num1:float=float(input("Enter the first number :"))
    num2:float=float(input("Enter the second number :"))
    remainder:float=num1%num2
    result:float=num1//num2
    print("The result of this division is " + str(result) + " with a remainder of " + str(remainder))
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()  
