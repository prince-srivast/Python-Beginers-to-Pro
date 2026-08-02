#=======================
#   Encapsulation
#=======================
 # Encapsulation hides internal object state and exposes a public interface.
 # Use private attributes and public methods to control access.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

account = BankAccount("Prince", 100)
account.deposit(50)
account.withdraw(30)
print("Balance:", account.get_balance())

# Direct access to __balance is not allowed
# print(account.__balance)  # AttributeError
