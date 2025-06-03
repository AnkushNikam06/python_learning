# Create a BankAccount class:
# It should have a private attribute __balance.
# It should have methods deposit(amount) and withdraw(amount) to modify the balance.
# It should have a method get_balance() to access the balance.
# Create a BankAccount object, deposit and withdraw some amount, and check the balance.

class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance +=amount
            print(f"Deposited: INR{amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew: INR{amount}")
            else:
                print("Insufficient funds.")
        else: 
            print("Withdrawal amount must be positive")

    def get_balance(self):
        return self.__balance
    
initial_amount = int(input("Enter the initial balance in INR: "))
account = BankAccount(initial_amount)

deposit_amount = int(input("Enter the deposit amount in INR: "))
account.deposit(deposit_amount)

withdraw_amount = int(input("Enter the amount you wish to withdraw: "))
account.withdraw(withdraw_amount)

print(f"Current account balance is: INR{account.get_balance()}")
