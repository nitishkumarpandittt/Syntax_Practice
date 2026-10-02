# Bank Account -> Deposite Money -> Withdraw Money -> Details -> Update Details -> Delete Account

import json
import random
import string
from pathlib import Path

class Bank:
    database = Path(__file__).parent / 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:  
                content = fs.read()
                data = json.loads(content) if content else []
        else:
            print("No such file exists")
    except Exception as err:
        print(f"Exception Occurred {err}")

    @staticmethod
    def update():
        with open(Bank.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))
    
    def createAccount(self):
        info = {
            "name": input("Name: "),
            "age": int(input("Age: ")),
            "email": input("E-Mail: "),
            "pin": int(input("PIN: ")),
            "account_no": 1122,
            "balance": 0
        }
        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Invalid Details")
        else:
            print(f"\n\nAccount Created: {info['account_no']}")
            for i in info:
                print(f"{i} : {info[i]}")

            Bank.data.append(info)
            Bank.update()

user = Bank()

print("\nMenu: ")
print("Press 1 for creating an account")
print("Press 2 to deposte money")
print("Press 3 to withdraw money")
print("Press 4 for details")
print("Press 5 for updating the details")
print("Press 6 for deleting the account")

res = int(input("Select Option: "))

if res == 1:
    user.createAccount()