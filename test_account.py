from account import *
import pytest

class Test(pytest.TestCase):

    def test_init(self):
        assert self.p1.get_name == 'Lucas'
        assert self.p1.get_balance == 10
        assert self.p2.get_name == 'Matthew'
        assert self.p1.get_balance == 20

    def test_deposit(self):
        assert self.p1.deposit(-2) is False
        assert self.p1.deposit(3) is True

        assert self.p2.deposit(-2) is False
        assert self.p2.deposit(3) is True

    def test_withdraw(self):
        assert self.p1.withdraw(11) is False
        assert self.p1.withdraw(-1) is False
        assert self.p1.withdraw(5) is True

        assert self.p2.withdraw(11) is False
        assert self.p2.withdraw(-1) is False
        assert self.p2.withdraw(5) is True

if __name__ == '__main__':
    pytest.main()
