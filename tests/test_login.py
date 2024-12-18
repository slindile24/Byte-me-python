# tests/test_login.py - Tests for the login functionality

import unittest
from banking_app.login import login

class TestLogin(unittest.TestCase):

    def test_valid_login(self):
        self.assertTrue(login("user1", "securepassword123"))

    def test_invalid_login_wrong_password(self):
        self.assertFalse(login("user1", "wrongpassword"))

    def test_invalid_login_nonexistent_user(self):
        self.assertFalse(login("nonexistent_user", "any_password"))

    def test_login_empty_username(self):
        with self.assertRaises(ValueError):
            login("", "password")

    def test_login_empty_password(self):
        with self.assertRaises(ValueError):
            login("user1", "")

    def test_login_special_characters_in_username(self):
        with self.assertRaises(ValueError):
            login("user!@#", "password")

if __name__ == "__main__":
    unittest.main()
