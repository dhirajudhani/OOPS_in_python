class Account: 
    ## Constructor to initialize account details 
    def __init__(self, account_number, account_holder, balance):
        self.__account_number = account_number ## private attribute
        self.account_holder = account_holder
        self.__balance = balance ## private attribute

    ## Add the money to the account
    def deposite(self, amount):
        if amount>0:
            self.__balance +=amount
            print(f'Deposited {amount} in your Account and new __balance is {self.__balance}')
        else: 
            print('Deposit amount must be positive')
    
    ## Withdraw the money from the accunt
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn {amount} from your account and new __balance is {self.__balance}")
        else: 
            print("Insufficient funds in the Account")
    
    ## Display __balance
    def display(self): 
        print('Account __balance is : ', self.__balance)






if __name__ == '__main__':
    acc1 = Account(account_number = 12345, account_holder = 'John Doe', balance = 100000)
    
    acc1.display()
    print(acc1.balance)

