def main():
    mass_input:float=float(input("Enter mass in kilograms: "))
    m:float=mass_input
    c:float=299792458.0  # Speed of light in m/s
    e:float=m*c**2 # Energy in joules
    print("e = m * C^2...")
    print("m = " + str(m) + " kg")
    print("C = " + str(c) + " m/s")
    
    print(str(e) + "joules of enegy!")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()