# tests/test_signup.py - Tests for the signup functionality

import unittest
from banking_app.signup import signup

class TestSignup(unittest.TestCase):

    def test_valid_signup(self):
        self.assertTrue(signup("newuser", "SecurePass123", "newuser@example.com"))

    def test_signup_with_existing_username(self):
        with self.assertRaises(ValueError):
            signup("existinguser", "password", "existing@example.com")

    def test_signup_invalid_email_format(self):
        with self.assertRaises(ValueError):
            signup("newuser", "password", "not-an-email")

    def test_signup_empty_username(self):
        with self.assertRaises(ValueError):
            signup("", "password", "user@example.com")

    def test_signup_empty_password(self):
        with self.assertRaises(ValueError):
            signup("newuser", "", "user@example.com")

    def test_signup_weak_password(self):
        with self.assertRaises(ValueError):
            signup("newuser", "123", "user@example.com")

    def test_signup_empty_email(self):
        with self.assertRaises(ValueError):
            signup("newuser", "password", "")

if __name__ == "__main__":
    unittest.main()
