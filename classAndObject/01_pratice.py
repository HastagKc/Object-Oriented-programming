# 1. Bank Account Management System:
# Create a class representing a bank account with methods to deposit, withdraw, and display balance.

# Creating class 
class Bank:
    # define init function to initilize attributes 
    def __init__(self,account_no,account_holder,total_balance = 0):
        self.account_no = account_no
        self.account_holder = account_holder
        self.total_balance = total_balance
        # these lines initialize the attributes (account_no, account_holder, and total_balance) of the instance with the values passed to the __init__ method when creating a new object of the class. The self keyword ensures that these attributes belong to the specific instance of the class being created.

    def deposit(self, deposite_amount):
        if deposite_amount < 0:
            print("Deposite amount can't be less than 0, please provide valid amount")
        else:
            self.total_balance += deposite_amount
            print(f"Rs {deposite_amount} is deposite sucessfully")

    def withdraw(self, withdraw_ammount):
        if self.total_balance < withdraw_ammount:
            print("Insufficent balance to withdraw")
        else: 
            self.total_balance -= withdraw_ammount
            print(f"Rs {withdraw_ammount} is withdraw sucessfully")

    def display_info(self):
        print(f"Account Number: {self.account_no}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Total Balance : {self.total_balance}")

# creating object 
account1 = Bank(account_holder='Kshittiz', account_no='123456789')
account1.deposit(10000)
account1.display_info()
account1.withdraw(5000)
account1.display_info()

account2 = Bank(account_no='8945675123', account_holder='Jhon')
account2.deposit(45000)
account2.display_info()