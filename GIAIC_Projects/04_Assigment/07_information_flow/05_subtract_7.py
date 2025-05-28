def main():
    try:
        num: int = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    result = subtract_seven(num)
    print(f"Original number: {num}")
    print("After subtracting 7:", result)

def subtract_seven(num: int) -> int:
    return num - 7

if __name__ == '__main__':
    main()