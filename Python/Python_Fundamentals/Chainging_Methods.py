class User:
  def __init__(self, name, balance):
    self.balance = balance
    self.name = name
  
  def make_withdraw(self, amount):
    self.balance -= amount
    return self
  
  def display_user_balance(self):
    print("User:",self.name,"- Balance: $",self.balance)
    return self

george = User("George", 100)
liam = User("Liam", 100)

george.make_withdraw(50).display_user_balance()
liam.make_withdraw(10).display_user_balance()
