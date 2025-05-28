import random

DONE_LIKELIHOOD = 0.3  # Probability that done() returns True

def done():
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    for i in range(1, 11):  # Count from 1 to 10
        if done():  # Check if done() returns True before printing the number
            return  # If done() is True, exit the function and return to main()
        print(i, end=" ")  # Print the number with a space after it

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.", end=" ")
    chaotic_counting()  # Call the chaotic_counting function
    print("I'm done.")  # This prints after chaotic_counting() finishes

# Run the program
if __name__ == "__main__":
    main()