def main():
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    total=0
    for fruit in fruits:
        number_user_want=input(f"How many {fruit} do you want :")
        if number_user_want != "":
            Fruits_value=float(number_user_want)*float(fruits[fruit])
            total+=Fruits_value
    print(f"Your total bill is  {total}$")
        

if __name__ == "__main__":
    main()
