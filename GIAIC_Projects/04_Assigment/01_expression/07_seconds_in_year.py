Days_Per_Year:int=365
Hours_per_day=24
Min_Per_Hour=60
Sec_Per_Hour=60
def main():
    """Number of seconds in a Year"""
    Number_of_seconds:int=Days_Per_Year*Hours_per_day*Min_Per_Hour*Sec_Per_Hour
    print("Number of seconds in a year is", Number_of_seconds)
    

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()