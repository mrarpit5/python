class bank:
	def __init__(self):
		self.amnt=0
		self.bal=5000

	def add_account(self):
		print("Enter your name")
		nm=str(input())
		print("Enter mobile No")
		mno=int(input())
		print("Enter last 4 digits of your mobile no")
		lmno=int(input())
		print("your account number is :- ",mno+lmno)

	def deposit(self):
		#print("Enter your account number")
		print("Enter Amount")
		self.amnt=int(input())
		self.bal=self.bal+self.amnt
		print("Total Balance ",self.bal)

	def withdrawal(self):
		print("Enter Amount")
		self.amnt=int(input())
		self.bal=self.bal-self.amnt
		print("Total Balance ",self.bal)

	def transfer_money(self):
		print("transfer money To(plz Enter account no. of opsition)")
		self.actno=int(input())
		print("Enter Amount")
		self.amnt=int(input())
		self.bal=self.bal-self.amnt
		print("Transfer",self.amnt , "to" , self.actno)
		print("Total Balance ",self.bal)

	def show_balance(self):
		print("Total Balance ",self.bal)



b1=bank()

print("1. Add Bank account")
print("2. Deposit of money")
print("3. Withdrawal operation")
print("4. Money transfer")
print("5. Show Balance")


ans="y"

while ans=="y":
	print("Enter your choice:-")
	ch=int(input())
	if(ch==1):
		b1.add_account()
	if(ch==2):
		b1.deposit()
	if(ch==3):
		b1.withdrawal()
	if(ch==4):
		b1.transfer_money()
	if(ch==5):
		b1.show_balance()
	print("repeat menu(only y/n)")
	ans=str(input())

