class User:
# Update the User class __init__ method
    def __init__(self, name, email):
        self.name = name
        self.email = email
# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to
        self.account = {
            "acct1" : BankAccount(0.02, 0),
            "acct2" : BankAccount(0.04, 5000)
        }

    
#Add a make_deposit method to the User class that calls on it's bank account's instance methods.
    def make_deposit(self, amount, acct):
        self.account[acct].deposit(amount)
        return self

#Add a make_withdrawal method to the User class that calls on it's bank account's instance methods.
    def make_withdraw(self, amount, acct):
        self.account[acct].withdraw(amount)
        return self

#Add a display_user_balance method to the User class that displays user's account balance
    def display_user_balance(self):
        print(f'User: {self.name}\nAcct1:\n{self.account["acct1"].display_account_info()}\nAcct2:\n{self.account["acct2"].display_account_info()}')
        return self

# SENPAI BONUS: Add a transfer_money(self, amount, other_user) method to the user class that takes an amount and a different User instance, and transfers money from the user's account into another user's account.
    def transfer_money(self, amount, my_acct, other_user, other_acct):
        self.account[my_acct].withdraw(amount)
        other_user.account[other_acct].deposit(amount)
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
        return f"Balance: {self.balance}\nInt. Rate: {self.int_rate}"

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
user1.display_user_balance()
user1.account["acct1"].deposit(10000)
user1.display_user_balance()

user2 = User("Aidee", "aidee@gmail.com")
user2.account["acct1"].deposit(10000)
user2.transfer_money(200, "acct1", user1, "acct2")
user2.display_user_balance()
user1.display_user_balance()