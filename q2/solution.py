class BankAccount:
  def __init__(self,balance):
    self.balance= balance
  def deposit(self,amount):
    if amount > 0 :
      self.balance += amount
      print(f"Deposited: {amount}, New Balance: {self.balance}")
    else:
      print("Enter valid amount to deposit.")
  def withdraw(self,amount):
    if amount<= self.balance:
      self.balance -= amount
      print(f"Withdrwan: {amount}, New Balance: {self.balance}")
    else:
      print("Not sufficient amount")
  def check_balance(self):
      print(f"Current Balance: {self.balance}")
amount = 230000
account = BankAccount(balance=50000)
account.deposit(amount)
account.withdraw(100000)
account.check_balance()