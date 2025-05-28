import random

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
    random_number=random.randint(MIN_VALUE,MAX_VALUE)
    print(random_number)

if __name__ == '__main__':
    for i in range(N_NUMBERS):
        main()