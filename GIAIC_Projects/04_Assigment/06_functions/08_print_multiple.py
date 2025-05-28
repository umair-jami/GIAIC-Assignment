def main():
    message=input("Enter the message :")
    msg_number=input("Enter a number of times to repeat your message :")
    print((message + " ")*int(msg_number))


if __name__ == '__main__':
    main()