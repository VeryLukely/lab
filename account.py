if __name__ == '__main__':

    class Account:
        """
        A class representing details for an account balance object
        """

        def __init__(self, name: str, balance=0):
            """
            Constructor to create initial state of an account balance object
            :param name: Person's first name.
            :param balance: Person's account balance.
            """

            self.account_one = Account(name)
            self.account_name = name
            self.account_balance = balance
            self.account_balance = 0
            self.p1 = Account('Lucas', 10)
            self.p2 = Account('Matthew', 20)

        def deposit(self, amount):
            """
            Method to add funds to an account balance.
            :param amount: Person's amount of funds to be added.
            :return: True if successful transaction, false if not successful.
            """
            if amount > 0:
                self.account_balance = self.account_balance + amount
                return True
            else:
                return False


        def withdraw(self, amount):
            """
            Method to withdraw funds from an account balance.
            :param amount: Person's amount of funds to be removed.
            :return: True is successful transaction, false if not successful.
            """
            if amount < 1:
                return False
            elif amount > self.account_balance:
                return False
            else:
                self.account_balance = self.account_balance - amount
                return True

        def get_balance(self):
            """
            Method to access a person's account balance.
            :return: Person's account balance.
            """
            return self.account_balance

        def get_name(self):
            """
            Method to access a person's name.
            :return: Person's first name.
            """
            return self.account_name
