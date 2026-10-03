# Bank logic only: no input() or print() here.
# Methods take values as arguments and raise ValueError with a message when
# something is wrong, so the same class works for the terminal (main.py)
# and the website (app.py).

import json
import random
import string
from pathlib import Path

MIN_AGE = 18
MAX_DEPOSIT = 10000


class Bank:
    database = Path(__file__).parent / 'data.json'

    def __init__(self):
        self.data = self.__load()

    # ---------- file handling ----------

    def __load(self):
        if not Bank.database.exists():
            return []
        with open(Bank.database) as fs:
            content = fs.read()
        data = json.loads(content) if content else []

        # older accounts saved the PIN as a number, keep everything as text
        for account in data:
            account['pin'] = str(account['pin'])
            account['account_no'] = str(account['account_no'])
        return data

    def __save(self):
        with open(Bank.database, 'w') as fs:
            json.dump(self.data, fs, indent=4)

    # ---------- helpers ----------

    def __generateAccountNo(self):
        existing = {account['account_no'] for account in self.data}
        while True:
            alpha = random.choices(string.ascii_uppercase, k=3)
            num = random.choices(string.digits, k=3)
            accId = alpha + num
            random.shuffle(accId)
            accId = "".join(accId)
            if accId not in existing:       # make sure no two accounts share a number
                return accId

    def __findAccount(self, accountNo, pin):
        for account in self.data:
            if account['account_no'] == accountNo and account['pin'] == pin:
                return account
        raise ValueError("Invalid account number or PIN")

    @staticmethod
    def __checkPin(pin):
        if len(pin) != 4 or not pin.isdigit():
            raise ValueError("PIN must be exactly 4 digits")

    @staticmethod
    def __checkEmail(email):
        if "@" not in email or "." not in email.split("@")[-1]:
            raise ValueError("Enter a valid e-mail address")

    # ---------- features ----------

    def createAccount(self, name, age, email, pin):
        name, email, pin = name.strip(), email.strip(), str(pin).strip()

        if not name:
            raise ValueError("Name can't be empty")
        if age < MIN_AGE:
            raise ValueError(f"You must be at least {MIN_AGE} years old")
        Bank.__checkEmail(email)
        Bank.__checkPin(pin)
        if any(account['email'] == email for account in self.data):
            raise ValueError("An account with this e-mail already exists")

        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "account_no": self.__generateAccountNo(),
            "balance": 0
        }
        self.data.append(info)
        self.__save()
        return dict(info)

    def login(self, accountNo, pin):
        return dict(self.__findAccount(accountNo.strip(), str(pin).strip()))

    def deposit(self, accountNo, pin, amount):
        account = self.__findAccount(accountNo, pin)
        if amount <= 0 or amount >= MAX_DEPOSIT:
            raise ValueError(f"Deposit must be between 1 and {MAX_DEPOSIT - 1}")
        account['balance'] += amount
        self.__save()
        return account['balance']

    def withdraw(self, accountNo, pin, amount):
        account = self.__findAccount(accountNo, pin)
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        if amount > account['balance']:
            raise ValueError(f"Insufficient balance (available: {account['balance']})")
        account['balance'] -= amount
        self.__save()
        return account['balance']

    def updateDetails(self, accountNo, pin, name="", email="", newPin=""):
        account = self.__findAccount(accountNo, pin)
        name, email, newPin = name.strip(), email.strip(), str(newPin).strip()

        # empty value means "keep the old one"
        if email:
            Bank.__checkEmail(email)
            if any(acc['email'] == email and acc is not account for acc in self.data):
                raise ValueError("An account with this e-mail already exists")
        if newPin:
            Bank.__checkPin(newPin)

        if name:
            account['name'] = name
        if email:
            account['email'] = email
        if newPin:
            account['pin'] = newPin
        self.__save()
        return dict(account)

    def deleteAccount(self, accountNo, pin):
        account = self.__findAccount(accountNo, pin)
        self.data.remove(account)
        self.__save()
