  
# Assignment: Convert Fahrenheit to Celsius using float
degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0
print(f"{degrees_fahrenheit}°F is equal to {degrees_celsius:.2f}°C")