
class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance


import unittest

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        """Create a BankAccount instance for testing."""
        self.account = BankAccount(owner="Alice", balance=100)

    def test_initial_balance(self):
        """Test the initial balance of the account."""
        self.assertEqual(self.account.balance, 100)

    def test_deposit_normal(self):
        """Test depositing a normal positive amount."""
        new_balance = self.account.deposit(50)
        self.assertEqual(new_balance, 150)

    def test_deposit_edge_case(self):
        """Test depositing a small positive amount."""
        new_balance = self.account.deposit(0.01)
        self.assertEqual(new_balance, 100.01)

    def test_deposit_invalid(self):
        """Test depositing a zero or negative amount raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.account.deposit(0)
        self.assertEqual(str(context.exception), "Deposit amount must be positive")

        with self.assertRaises(ValueError) as context:
            self.account.deposit(-10)
        self.assertEqual(str(context.exception), "Deposit amount must be positive")

    def test_withdraw_normal(self):
        """Test withdrawing a normal amount."""
        new_balance = self.account.withdraw(50)
        self.assertEqual(new_balance, 50)

    def test_withdraw_edge_case(self):
        """Test withdrawing the exact balance."""
        new_balance = self.account.withdraw(100)
        self.assertEqual(new_balance, 0)

    def test_withdraw_insufficient_funds(self):
        """Test withdrawing an amount greater than the balance raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(150)
        self.assertEqual(str(context.exception), "Insufficient funds")

    def test_withdraw_negative_amount(self):
        """Test withdrawing a negative amount raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(-20)
        self.assertEqual(str(context.exception), "Insufficient funds")

if __name__ == '__main__':
    unittest.main()
