def main():
    fruits = list_stock()
    print("Available fruits:", ", ".join(fruits.keys()))
    fruit = input("Enter a fruit: ").strip().lower()
    stock = num_in_stock(fruit, fruits)
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)

def list_stock():
    return {
        'apple': 2,
        'durian': 4,
        'pear': 1000,
        'banana': 12,
        'orange': 8
    }

def num_in_stock(fruit, fruits):
    """
    This function returns the number of fruit Sophia has in stock.
    """
    return fruits.get(fruit, 0)

if __name__ == '__main__':
    main()