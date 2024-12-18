import unittest
from unittest.mock import patch
from banking_app.transaction import transact

class TestTransaction(unittest.TestCase):

    def setUp(self):
        """Mock user database for transactions."""
        self.mock_users = [
            {"username": "johndoe", "password": "hashed_password", "email": "johndoe@example.com", "account_id": "account1", "balance": 1000.50},
            {"username": "janedoe", "password": "hashed_password2", "email": "janedoe@example.com", "account_id": "account2", "balance": 500.00},
        ]

    def mock_read_users(self):
        """Simulate reading from the mock user database."""
        return self.mock_users

    def mock_write_users(self, users):
        """Simulate writing to the mock user database."""
        self.mock_users = users

    @patch("banking_app.user_management.read_users", side_effect=mock_read_users)
    @patch("banking_app.user_management.write_users", side_effect=mock_write_users)
    def test_valid_transaction(self, mock_read, mock_write):
        """Test a valid transaction."""
        self.assertTrue(transact("account1", "account2", 200.00))
        # Check updated balances
        self.assertEqual(self.mock_users[0]["balance"], 800.50)  # John Doe
        self.assertEqual(self.mock_users[1]["balance"], 700.00)  # Jane Doe

    @patch("banking_app.user_management.read_users", side_effect=mock_read_users)
    def test_transaction_insufficient_funds(self, mock_read):
        """Test transaction fails due to insufficient funds."""
        with self.assertRaises(ValueError):
            transact("account2", "account1", 1000.00)  # Jane Doe doesn't have enough funds

    @patch("banking_app.user_management.read_users", side_effect=mock_read_users)
    def test_transaction_negative_amount(self, mock_read):
        """Test transaction fails for negative amount."""
        with self.assertRaises(ValueError):
            transact("account1", "account2", -100.00)

    @patch("banking_app.user_management.read_users", side_effect=mock_read_users)
    def test_transaction_zero_amount(self, mock_read):
        """Test transaction fails for zero amount."""
        with self.assertRaises(ValueError):
            transact("account1", "account2", 0)

    @patch("banking_app.user_management.read_users", side_effect=mock_read_users)
    def test_transaction_invalid_account(self, mock_read):
        """Test transaction fails for invalid accounts."""
        with self.assertRaises(ValueError):
            transact("invalid_account", "account2", 100.00)

    @patch("banking_app.user_management.read_users", side_effect=mock_read_users)
    def test_transaction_same_account(self, mock_read):
        """Test transaction fails when sender and receiver are the same."""
        with self.assertRaises(ValueError):
            transact("account1", "account1", 100.00)

if __name__ == "__main__":
    unittest.main()
