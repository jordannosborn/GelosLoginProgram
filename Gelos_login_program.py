import random
import time


# login the user
def login():
    userName = input("Please enter your username: ")
    password = input("Please enter your password: ")
    with open('accounts.txt') as f:
        lines = f.readlines()
        if userName + " " + password + "\n" in lines:
            print("Congratulations! You have been logged in. ")
        else:
            print("Your username or password is incorrect, please try again. ")


# register the user
def register():
    userName = input("Please create a username: ")
    generatePassword = input("Would you like a randomly generated password? (y/n): ")

    # generate a random password
    if generatePassword == "y":
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"
        password_len = 10
        password = ""
        for x in range(0, password_len):
            password_char = random.choice(chars)
            password = password + password_char
        print("Here is your random password: ", password)

    # let the user enter their own password
    else:
        password = input("Please choose a password (we recommend 10 characters): ")

    f = open("accounts.txt", "a")
    f.write("\n" + userName + " " + password)
    f.close()
    print("Thank you! Your account has been registered. ")


# show all username and passwords.
# this should only be usable by admins
def view_accounts():
    print("List of user accounts: ")
    with open('accounts.txt') as f:
        lines = f.readlines()
        for line in lines:
            print(line)


# exit the program
def exit_program():
    time.sleep(2)  # Sleep for 2 seconds
    exit()

# main menu
# loop program
while 1:
    print("1. login")
    print("2. register")
    print("3. view accounts")
    print("4. exit program")
    option = input("Please select a number: ")
    if option == "1":
        login()
    elif option == "2":
        register()
    elif option == "3":
        view_accounts()
    elif option == "4":
        exit_program()
    else:
        print("Please select one of the options. ")

