# 🏧 ATM Machine

# Is project mein aap use karenge:

# Features:              | Concepts:
# 1. PIN Check           | while loop
# 2. Balance Check       | if-else
# 3. Deposit             | functions
# 4. Withdraw            | variables
# 5. Exit                | input
#                         | operators


# ------------------------------------------
# Bank Data
# ------------------------------------------

user_balance = 1000
pin = "123456"


# ------------------------------------------
# PIN Check Function
# ------------------------------------------

def pin_check():

    while True:

        user_pin = input("Enter your PIN: ")

        if user_pin == pin:
            print("PIN is correct")
            break

        else:
            print("PIN is incorrect")


# ------------------------------------------
# Balance Check Function
# ------------------------------------------

def balance_check():
    print("Your balance is:", user_balance)


# ------------------------------------------
# Deposit Function
# ------------------------------------------

def deposit():
    global user_balance

    deposit_amount = float(input("Enter the amount to deposit: "))

    user_balance = user_balance + deposit_amount

    print("Amount deposited successfully")
    print("Your updated balance is:", user_balance)


# ------------------------------------------
# Withdraw Function
# ------------------------------------------

def with_draw():
    global user_balance

    withdraw_amount = float(input("Enter the amount to withdraw: "))

    if withdraw_amount <= user_balance:

        user_balance = user_balance - withdraw_amount

        print("Amount withdrawn successfully")
        print("Your updated balance is:", user_balance)

    else:

        print("Insufficient balance")


# ------------------------------------------
# ATM Machine
# ------------------------------------------

print("Welcome to the ATM machine")

pin_check()


# ------------------------------------------
# Main Menu
# ------------------------------------------

while True:

    print("\n----- ATM MENU -----")
    print("1. Balance Check")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        balance_check()

    elif choice == "2":

        deposit()

    elif choice == "3":

        with_draw()

    elif choice == "4":

        print("Thank you for using the ATM machine")
        break

    else:

        print("Invalid choice. Please try again")