def get_user_info():
    while True:
        first_name = input("What is your first name?: ").strip()
        if first_name:
            break
        print("First name cannot be empty.")

    while True:
        last_name = input("What is your last name?: ").strip()
        if last_name:
            break
        print("Last name cannot be empty.")

    while True:
        email_address = input("What is your email address?: ").strip()
        if email_address:
            break
        print("Email address cannot be empty.")

    return first_name, last_name, email_address


def main():
    user_data = get_user_info()
    print("Received the following user data:")
    print(f"First Name: {user_data[0]}")
    print(f"Last Name: {user_data[1]}")
    print(f"Email Address: {user_data[2]}")

if __name__ == "__main__":
     main()