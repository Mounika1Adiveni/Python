class SBI_BANK_ACCOUNT:
    def __init__(self, AccountNumber,balance):
        self.AccountNumber = AccountNumber
        self.__balance = balance
#getter
    def get_balance(self):
        return self.__balance
#setter
    def set_balance(self,amount):
        if amount > 0:
            self.__balance=amount
        else:
            print("the balance cannot be less than zero")
#deposit _money
    def deposit_money(self,amount):
        if amount>0:
         self.__balance=self.__balance+amount
        else:
            print("negative balance could not be deposited")
#withdrawl method
    def withdraw_money(self,amount):
        if 0<amount<= self.get_balance():
            self.__balance=self.__balance -amount
        else:
            print("negative balance could not be withdrawn")
account_mine = SBI_BANK_ACCOUNT(100000000,20000)
print(account_mine.get_balance())
account_mine.deposit_money(3000)
print(account_mine.get_balance())
account_mine.withdraw_money(2000)
print(account_mine.get_balance())
account_mine.withdraw_money(21000)
print(account_mine.get_balance())

