
class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit of {amount} successful. Current balance: {self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal of {amount} successful. Current balance: {self.balance}"
        else:
            return "Insufficient funds."


class SavingsAccount(Account):
    def __init__(self, account_number, interest_rate, balance=0):
        super().__init__(account_number, balance) # calling parent function to initilize balance and account_number
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        return f"Interest of {interest} credited. Current balance: {self.balance}"


class CheckingAccount(Account):
    def __init__(self, account_number, transaction_fee, balance=0):
        super().__init__(account_number, balance)
        self.transaction_fee = transaction_fee

    def deduct_transaction_fee(self):
        self.withdraw(self.transaction_fee)
        return f"Deducted transaction fee of {self.transaction_fee}. Current balance: {self.balance}"


# Creating instances
savings_acc = SavingsAccount(account_number="SA123",interest_rate= 0.05)



# checking_acc = CheckingAccount("CA456", 2, 500)

# # Depositing and withdrawing from savings account
savings_acc.deposit(2000)
savings_acc.withdraw(1500)

print(f'Details: \n Account_no:{savings_acc.account_number} \n Total Balance: {savings_acc.balance} \n Interest rate: {savings_acc.interest_rate}')

# # Calculating interest for savings account
# print(savings_acc.calculate_interest())

# # Depositing and deducting transaction fee from checking account
# print(checking_acc.deposit(200))
# print(checking_acc.deduct_transaction_fee())
