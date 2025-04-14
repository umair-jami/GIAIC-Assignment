def main():
    Anton_age:int=21
    print("Anton is " + str(Anton_age))
    Beth_age:int=Anton_age+6
    print("Beth is " + str(Beth_age))
    Chen_age:int=Beth_age+20
    print("Chen is " + str(Chen_age))
    Drew_Age:int=Chen_age + Anton_age
    print("Drew is " + str(Drew_Age))
    Ethan_age:int=Chen_age
    print("Ethan is " + str(Ethan_age))
    

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()