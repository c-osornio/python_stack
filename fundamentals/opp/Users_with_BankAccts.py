class User:
# Update the User class __init__ method
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
#Add a make_deposit method to the User class that calls on it's bank account's instance methods.
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

#Add a make_withdrawal method to the User class that calls on it's bank account's instance methods.
    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self

#Add a display_user_balance method to the User class that displays user's account balance
    def display_user_balance(self):
        self.account.display_account_info()
        return self

# SENPAI BONUS: Add a transfer_money(self, amount, other_user) method to the user class that takes an amount and a different User instance, and transfers money from the user's account into another user's account.
    def transfer_money(self, amount, other_user):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self

class BankAccount:
    all_accts = []

    def __init__(self, int_rate,balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficent funds: Charging a $5 fee")
            self.balance -+ 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}\nInt. Rate: {self.int_rate}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = round((self.balance * self.int_rate) + self.balance, 2)
        else:
            print(f"Insufficent funds to yield interest")
        return self

    @classmethod
    def print_accts(cls):
        for accounts in cls.all_accts:
            accounts.display_account_info()

user1 = User("Charlie", "charlie@gmail.com")
user1.account.display_account_info()
user1.account.deposit(10000)
user1.account.display_account_info()

user2 = User("Aidee", "aidee@gmail.com")
user2.account.deposit(10000)
user2.transfer_money(200, user1)
user2.display_user_balance()