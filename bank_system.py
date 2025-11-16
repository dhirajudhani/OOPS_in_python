class Account: 
    ## Constructor to initialize account details 
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    ## Add the money to the account
    def deposite(self, amount):
        if amount>0:
            self.balance +=amount
            print(f'Deposited {amount} in your Account and new balance is {self.balance}')
        else: 
            print('Deposit amount must be positive')
    
    ## Withdraw the money from the accunt
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount} from your account and new balance is {self.balance}")
        else: 
            print("Insufficient funds in the Account")
    
    ## Display balance
    def display(self): 
        print('Account Balance is : ', self.balance)



## Inheritance  : Saving account inherits from account 
class SavingAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate ):
        super().__init__(account_number, account_holder, balance) ## takes the all existing value from parent class
        self.interest_rate = interest_rate
        
    ## Polymorphism (Overriding the same name methods): Display the account details   
    def display(self): 
        print(f"Account Balance is : {self.balance},  Interest Rate : {self.interest_rate}%")

    ## Added the interest in saving accounts
    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest added {interest}. New balance is {self.balance}")
        
        
        
    
        
## Inheritance  : Current account inherits from account 
class CurrentAccount(Account):
    def __init__(self, account_number, account_holder, balance, od_limit):
        super().__init__(account_number, account_holder, balance) ## takes the all existing value from parent class
        self.od_limit = od_limit
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance + self.od_limit:
            self.balance  -= amount
            print(f'withdraw amount {amount} and New balance is {self.balance}')
        else:
            print("Insufficient funds in the Account")

    def display(self):
        print(f'Current account details balance is : {self.balance}, OD Limit is : {self.od_limit}')






if __name__ == '__main__':
    acc1 = SavingAccount("A001", "Anil", 100000, 10)
    acc2 = CurrentAccount( "B002", "Beni", 100000, 10000)
    
    
    acc1.deposite(20000)
    acc1.add_interest()
    acc1.display()
    
    
    acc2.deposite(50000)
    acc2.display()
    acc2.withdraw(125000)




## Abstraction : abstraction in python is a core principle of the oops that simplifies complex systems by focusing on essential characteristics while hiding unnecessary details 

## Encapsulation :  encapsulation in python is a mechanism where data and methods are bound together within an object.


## attribute vs methods in python : attribute refers to the value or value of any given variable, method refers to a function that can be called by other functions.
                     
