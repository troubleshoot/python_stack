class User:
	def __init__(self, name, email):
		self.email = email
		self.name = name
		self.account = BankAccount(int_rate = 0.02, balance = 0)
	
	def display_user_balance(self):
		print("User:",self.name,"- Balance: $",self.account.display_balance())
		return self
	
	def make_deposit(self, amount):
		self.account.deposit(amount)

	def make_withdraw(self, amount):
		self.account.withdraw(amount)


class BankAccount:
	def __init__(self, int_rate, balance):
		self.balance = balance
		self.int_rate = int_rate
	
	def deposit(self, amount):
		self.balance += amount
		return self
	
	def withdraw(self, amount):
		self.balance -= amount
		return self
	
	def display_balance(self):
		return self.balance
	
	def yield_interest(self):
		if(self.balance > 0):
			self.balance += self.balance * (self.int_rate * .01)
		else:
			print("Positive balance needed")
		return self

george = User("George", "george@gmail.com")

george.display_user_balance()
george.make_deposit(50)
george.display_user_balance()
george.make_withdraw(150)
george.display_user_balance()
