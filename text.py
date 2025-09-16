class Atm:
    def __init__(self):
     self.pin=0
     self.balance=0
     self.menu()
    
    def menu(self):
     print("""
              HI!
              HOW CAN I HELP YOU?
              1.press 1 to create pin
              2.press 2 to change pin
              3.press 3 to check balance
              4.press 4 to withdraw
              5.press 5 to deposit
              6.press anything to exit
              """)
    
     user_input=int(input("enter your choice"))
     if user_input==1:
        self.create_pin()
     elif user_input==2:
        self.change_pin()
     elif user_input==3:
        self.check_balance()
     elif user_input==4:
        self.withdraw()
     elif user_input==5:
        self.deposit()
     else:
         print("Error!!!!!")
         exit()
    

    def verify_pin(self):
     for i in range(3):
        user_pin = (input("Enter your pin: "))
        if user_pin == self.pin:
            print("PIN verified successfully.")
            return 1
        else:
            print(f"Incorrect pin. Attempts left: {2 - i}")
     return 0

            
               
        
            
    def create_pin(self):
        user_pin=(input("enter your pin:"))
        if len(user_pin)!=4 or not user_pin.isdigit():
            print("enter 4 digit valid pin ")
            self.menu()
            return
        
        self.pin=user_pin
        print("pin set successfully")
        
        user_balance=int(input("enter your balance:"))
        if user_balance<0:
            print("invalid balance")
            
        else:
            self.balance=user_balance
            print("your balance is:",self.balance)
            print("account created successfully")
            self.menu()
            
    def change_pin(self):
        user_oldpin=input("enter your old pin:")
        if user_oldpin!=self.pin:
            print("incorrect pin")
            self.menu()
            return
        user_newpin=input("enter your new pin:")
        if len(user_newpin)!=4 or not user_newpin.isdigit():
                 print("enter 4 digit valid pin")
        else:
                self.pin=user_newpin
                print("pin changed successfully")
                self.menu()
    def check_balance(self):
     if self.verify_pin():
            print("your balance is",self.balance)
            self.menu()
            
     else:
             print("Wrong pin try again later")
             self.menu()
             
    def withdraw(self):
     if self.verify_pin():
        amount=int(input("enter amount to withdraw:"))
        if amount>self.balance:
            print("insufficient balance")
            self.menu()
        else:
         self.balance-=amount
         print("withdraw successful")
         print("your balance is:",self.balance) 
         self.menu()
     else:
         print("attempts over")
         self.menu()
        
    def deposit(self):
        if self.verify_pin():
         amount=int(input("enter amount to deposit:"))
         if amount<=0:
            print("invalid amount")
            self.menu()
         else:
                self.balance+=amount
                print("deposit successful")
                print("your balance is:",self.balance)
                self.menu()
obj=Atm()
                
        
        
            
    
        
    