import math
def main():
    ab:float=float(input("Enter the length of ab :"))
    ac:float=float(input("Enter the length of ac :"))
    bc:float=math.sqrt(ab**2+ac**2)
    print("The length of bc is",bc)
if __name__ == '__main__':
    main()