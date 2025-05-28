import random
def main():
    # random number
    random_num=random.randint(1,99)
    print(random_num)
    print("I am thinking of a number between 1 and 99")

    guess=int(input("Enter a guess: "))
    while guess != random_num:
        if guess < random_num:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        print() 
        guess=int(input("Enter a guess: "))
    print("Congrats! The number was: " + str(random_num))
    
if __name__ == '__main__':
    main()