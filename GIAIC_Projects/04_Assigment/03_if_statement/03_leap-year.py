def main():
    Enter_Year=int(input("Enter Year in Numbers :"))
    if Enter_Year % 4 ==0:
        if Enter_Year %100==0:
            if Enter_Year % 400 ==0:
                print(f"{Enter_Year} is Leap Year")
            else:
                print(f"{Enter_Year} is not a Leap Year")
        else:
            print(f"{Enter_Year} is Leap Year")
    else:
        print("This is not leap year")


if __name__ == '__main__':
    main()