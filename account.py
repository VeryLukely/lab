if __name__ == '__main__':

    class Account:
        def __init__(self, name):

            self.account_one = Account(name)
            self.account_name = name
            self.account_balance = 0

        def deposit(self, amount):
            if amount > 0:
                self.account_balance = self.account_balance + amount
                return True
            else:
                return False

        def withdrawl(self, amount):
            if amount < 1:
                return False
            elif amount > self.account_balance:
                return False
            else:
                self.account_balance = self.account_balance - amount
                return True

        def get_balance(self):
            return self.account_balance

        def get_name(self):
            return self.account_name
    