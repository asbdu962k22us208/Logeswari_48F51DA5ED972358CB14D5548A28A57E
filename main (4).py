class Bank_account:
  def__init__(self.):
      self.__name=str(input("enter the name of account holder: "))    
      self.__ano-int(input("enter the type of account number: "))
      self.__balance=0 
      print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
  def deposit (self):
    amount=float(input("Enter amount to be "))
   if amoun>0:
      self. balance += amount print("\n Amount Deposited: amount)
  def withdraw(self):
   amount = float(input("Enter amount to be Withdrawn:")
    if self. balance>= amount: 
       self.__balance-= amount)
       print("\n You Withdrew:", amount)
       print("\n Balance: ", self._ balance)
    else:
        print("\n Insufficient balance")
  def display(self):
    print("\n Accountholder name: ", self. name) 
    print("\n Account Number: ", self.__ano) 
    print("\n Net Available Balance=",self.___balance)
s = Bank_Account()
s.deposit()
s.withdraw() 
s.display()