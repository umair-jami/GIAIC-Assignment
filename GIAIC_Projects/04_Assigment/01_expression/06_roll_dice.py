"""Simulate rolling two dice and prints results of each roll as well as the total"""
import random

DICE_SIDES:int=6
def main():
    dice1=random.randint(1,DICE_SIDES)
    dice2=random.randint(1,DICE_SIDES)
    
    total:int=dice1+dice2
    print("Dice have", DICE_SIDES, "sides each.")
    print("First die:", dice1)
    print("Second die:", dice2)
    print("Total of two dice:", total)
    
if __name__ == "__main__":
    main()