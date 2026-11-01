class BankAccount:
    def __init__(self, account_number, holder_name, account_type, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.balance = self.balance + amount
            print("Deposit successful.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance = self.balance - amount
            print("Withdrawal successful.")

    def display_details(self):
        print("Account number:", self.account_number)
        print("Account holder:", self.holder_name)
        print("Account type:", self.account_type)
        print("Balance:", format(self.balance, ".2f"))


account = BankAccount("1001", "Anu", "Savings", 1000.0)
account.deposit(float(input("Enter deposit amount: ")))
account.withdraw(float(input("Enter withdrawal amount: ")))
account.display_details()
