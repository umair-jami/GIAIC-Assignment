def main():
    """Convert feet to inches."""
    feet_input:float=float(input("Enter feet: "))
    feet:float=feet_input
    inches:float=feet*12.0 # Convert feet to inches
    print(str(feet) + " feet is " + str(inches) + " inches.")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()