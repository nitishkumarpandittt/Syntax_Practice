# Terminal version of the bank
# Bank Account -> Deposit Money -> Withdraw Money -> Details -> Update Details -> Delete Account
# The website version is app.py (run: streamlit run app.py)

from bank import Bank


def askInt(prompt):
    # keep asking until the user types a whole number
    while True:
        value = input(prompt)
        if value.strip().lstrip("-").isdigit():
            return int(value)
        print("Please enter a number")


def showAccount(account):
    print("\nUser Details: ")
    for key in account:
        if key != 'pin':                    # never print the PIN
            print(f"{key} : {account[key]}")


def createAccount(bank):
    account = bank.createAccount(
        name=input("Name: "),
        age=askInt("Age: "),
        email=input("E-Mail: "),
        pin=input("PIN (4 digits): ")
    )
    print(f"\nAccount Created! Your account number is {account['account_no']}")
    print("Save it, you'll need it to log in.")
    showAccount(account)


def depositMoney(bank):
    accountNo, pin = input("Account number: "), input("Enter PIN: ")
    bank.login(accountNo, pin)              # check details before asking the amount
    balance = bank.deposit(accountNo, pin, askInt("Amount to deposit: "))
    print(f"Amount deposited successfully. New balance: {balance}")


def withdrawMoney(bank):
    accountNo, pin = input("Account number: "), input("Enter PIN: ")
    bank.login(accountNo, pin)
    balance = bank.withdraw(accountNo, pin, askInt("Amount to withdraw: "))
    print(f"Amount withdrawn successfully. New balance: {balance}")


def showDetails(bank):
    showAccount(bank.login(input("Account number: "), input("Enter PIN: ")))


def updateDetails(bank):
    accountNo, pin = input("Account number: "), input("Enter PIN: ")
    bank.login(accountNo, pin)
    print("Fill the details or press Enter to skip: ")
    account = bank.updateDetails(
        accountNo, pin,
        name=input("New name: "),
        email=input("New e-mail: "),
        newPin=input("New PIN: ")
    )
    print("Details updated successfully")
    showAccount(account)


def deleteAccount(bank):
    accountNo, pin = input("Account number: "), input("Enter PIN: ")
    bank.login(accountNo, pin)
    if input("Type YES to permanently delete your account: ") == "YES":
        bank.deleteAccount(accountNo, pin)
        print("Account deleted")
    else:
        print("Cancelled")


options = {
    1: ("Create an account", createAccount),
    2: ("Deposit money", depositMoney),
    3: ("Withdraw money", withdrawMoney),
    4: ("Show details", showDetails),
    5: ("Update details", updateDetails),
    6: ("Delete account", deleteAccount),
}

bank = Bank()

while True:
    print("\nMenu: ")
    for number, (label, _) in options.items():
        print(f"Press {number} to {label.lower()}")
    print("Press 0 to exit")

    choice = askInt("Select Option: ")
    if choice == 0:
        print("Thank you for banking with us!")
        break
    if choice not in options:
        print("Invalid option")
        continue

    try:
        options[choice][1](bank)
    except ValueError as err:               # every bank error comes here
        print(f"Error: {err}")
