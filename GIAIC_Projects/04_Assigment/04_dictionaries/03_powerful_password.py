from hashlib import sha256

def login(email,saves_login,pass_check):
    """ Returns True if the hash of the password we are checking matches the one in stored_logins
    for a specific email. Otherwise, returns False.
"""
    if saves_login[email]==hash_pass(pass_check):
        return True
    return False


def hash_pass(pass_check):
    """Takes in a password and returns the SHA256 hashed value for that specific password."""
    return sha256(pass_check.encode()).hexdigest()

def main():
    # stored_logins is a dictionary with emails as keys and hashed passwords as values
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"
    }
    email_input=input("Enter Your Email to add data :")
    pass_input=input("Enter the pass to add data :")
    pass_hash_value= hash_pass(pass_input)
    stored_logins[email_input]=pass_hash_value
    # for searching data
    check_email=input("Enter the email for checking data :")
    check_pass=input("Enter the password for checking data :")
    print(login(check_email,stored_logins,check_pass))
    
if __name__ == '__main__':
    main()