def main():
    number = input("Enter the Number for Doubling: ")
    while number:
        number = int(number)  # Convert input to an integer
        if number <= 100:
            print(number * 2)
        else:
            print("Number should be less than 100")
        number = input("Enter the Number for Doubling: ")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()