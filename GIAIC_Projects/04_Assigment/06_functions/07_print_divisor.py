def main():
    input_number = input("Enter the number: ")
    lst = []  # Initialize the list outside the loop
    for i in range(1, int(input_number) + 1):
        if int(input_number) % i == 0:
            lst.append(i)  # Append divisors to the list
    print(f"Here is the list of all divisors of {input_number}: {lst}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()