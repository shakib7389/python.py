class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}")
        else:
            print("Invalid deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}")
        else:
            print("Invalid withdrawal.")

    def check_balance(self):
        print(f"Balance: ${self.balance}")

def main():
    account = BankAccount(input("Name: "))
    while True:
        print("\n1.Deposit 2.Withdraw 3.Balance 4.Exit")
        choice = input("Choose: ")
        if choice == "1":
            account.deposit(float(input("Amount: ")))
            account.check_balance()
        elif choice == "2":
            account.withdraw(float(input("Amount: ")))
            account.check_balance()
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()