class BankAccount:
    all_accts = []

    def __init__(self, int_rate,balance = 0): #defult balance at zero if no amount is given
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

#NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
    @classmethod
    def print_accts(cls):
        for accounts in cls.all_accts:
            accounts.display_account_info()

acct1 = BankAccount(.01, 1000)
acct2 = BankAccount(.04, 7500)

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
acct1.deposit(150.75).deposit(11.51).deposit(2520.75).withdraw(1500).yield_interest().display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
acct2.deposit(119.33).deposit(5899.99).withdraw(500).withdraw(500).yield_interest().display_account_info()

#NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
BankAccount.print_accts()