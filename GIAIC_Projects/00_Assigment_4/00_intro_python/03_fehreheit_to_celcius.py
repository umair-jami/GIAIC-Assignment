def main():
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    degrees_celsius=(degrees_fahrenheit - 32) * 5.0/9.0
    print(f"{degrees_fahrenheit}°F is equal to {degrees_celsius:.2f}°C")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()