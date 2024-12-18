import unittest
import os
from tempfile import NamedTemporaryFile

# Import the function stubs for testing
from functions_to_test import *
class TestPythonBasics(unittest.TestCase):

    # Test arithmetic function: add_numbers
    def test_add_numbers(self):
        self.assertEqual(add_numbers(3, 5), 8)
        self.assertEqual(add_numbers(-3, 5), 2)
        self.assertEqual(add_numbers(0, 0), 0)
        with self.assertRaises(TypeError):
            add_numbers(3, "five")  # Invalid input


    def test_fibonacci_0_and_1(self):
        self.assertEqual([fibonacci(n) for n in range(0)],
        [])
        self.assertEqual([fibonacci(n) for n in range(1)],
        [0])
        self.assertEqual([fibonacci(n) for n in range(2)],
        [0,1])


    def test_fibonacci_15(self):
        self.assertEqual([fibonacci(n) for n in range(15)],
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377])


    def test_fibonacci_30(self):
        self.assertEqual([fibonacci(n) for n in range(30)],
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 
        610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 
        75025, 121393, 196418, 317811, 514229])


    def test_factorial_0_and_1(self):
        self.assertEqual(factorial(0),
        1)
        self.assertEqual(factorial(1),
        1)


    def test_factorial_negative(self):
        self.assertEqual(factorial(-1),
        "")

    
    def test_factorial_5(self):
        self.assertEqual(factorial(5),
        120)


    def test_factorial_10(self):
        self.assertEqual(factorial(10),
        3628800)


    # Test maximum-finding function
    def test_find_maximum(self):
        self.assertEqual(find_maximum(1, 5, 3), 5)
        self.assertEqual(find_maximum(-1, -5, -3), -1)
        self.assertEqual(find_maximum(7, 7, 7), 7)
        with self.assertRaises(TypeError):
            find_maximum(1, "five", 3)  # Mixed types

    # Test palindrome checker
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertFalse(is_palindrome("python"))
        self.assertTrue(is_palindrome("level"))
        with self.assertRaises(TypeError):
            is_palindrome(12321)  # Input not a string

    # Test word counting in a string
    def test_count_word_occurrences(self):
        text = "Python is great. Python is versatile."
        self.assertEqual(count_word_occurrences(text, "python"), 2)
        self.assertEqual(count_word_occurrences(text, "is"), 2)
        self.assertEqual(count_word_occurrences(text, "java"), 0)
        with self.assertRaises(TypeError):
            count_word_occurrences(12345, "python")  # Non-string text

    # Test file reading functionality
    def test_read_file_lines(self):
        with NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(b"Hello\nWorld\nPython\n")
            temp_file_path = temp_file.name

        try:
            lines = read_file_lines(temp_file_path)
            self.assertEqual(lines, ["Hello\n", "World\n", "Python\n"])
            with self.assertRaises(FileNotFoundError):
                read_file_lines("non_existent_file.txt")  # Non-existent file
        finally:
            os.remove(temp_file_path)

    # Test factorial calculation
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        with self.assertRaises(ValueError):
            factorial(-3)  # Factorial of negative number
        with self.assertRaises(TypeError):
            factorial("five")  # Invalid input type

    # Test prime number checker
    def test_is_prime(self):
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(9))
        self.assertTrue(is_prime(2))
        with self.assertRaises(ValueError):
            is_prime(-5)  # Prime not defined for negative numbers
        with self.assertRaises(TypeError):
            is_prime("eleven")  # Invalid input type

    # Test sorting functionality
    def test_sort_numbers(self):
        self.assertEqual(sort_numbers([3, 1, 4, 1, 5, 9]), [1, 1, 3, 4, 5, 9])
        self.assertEqual(sort_numbers([]), [])
        self.assertEqual(sort_numbers([-3, -1, -2]), [-3, -2, -1])
        with self.assertRaises(TypeError):
            sort_numbers(["three", "one", "four"])  # Invalid input type

    # Test person object
    def test_person(self):
        person = Person(name="Alice", age=30)
        self.assertEqual(person.name, "Alice")
        self.assertEqual(person.age, 30)
        with self.assertRaises(TypeError):
            Person(name="Bob", age="thirty")  # Invalid age type
        with self.assertRaises(TypeError):
            Person(name=123, age=25)  # Invalid name type

    def test_tower_of_hanoi_1(self):
        self.assertEqual(tower_of_hanoi(1, 'A', 'B', 'C'), [('A', 'C')])

    def test_tower_of_hanoi_2(self):
        self.assertEqual(tower_of_hanoi(2, 'A', 'B', 'C'), [('A', 'B'), ('A', 'C'), ('B', 'C')])

    def test_tower_of_hanoi_3(self):
        self.assertEqual(tower_of_hanoi(3, 'A', 'B', 'C'), [('A', 'C'), ('A', 'B'), ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C')])

    def test_tower_of_hanoi_4(self):
        self.assertEqual(tower_of_hanoi(4, 'A', 'B', 'C'), [
            ('A', 'C'), ('A', 'B'), ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C'),
            ('A', 'B'), ('C', 'B'), ('C', 'A'), ('B', 'A'), ('C', 'B'), ('A', 'C'), ('A', 'B'),
            ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C'), ('A', 'B'), ('C', 'B'),
            ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C')
        ])

    def test_tower_of_hanoi_5(self):
        self.assertEqual(tower_of_hanoi(5, 'A', 'B', 'C'), [
            ('A', 'C'), ('A', 'B'), ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C'),
            ('A', 'B'), ('C', 'B'), ('C', 'A'), ('B', 'A'), ('C', 'B'), ('A', 'C'), ('A', 'B'),
            ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C'), ('A', 'B'), ('C', 'B'),
            ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C'),
            ('A', 'B'), ('C', 'B'), ('C', 'A'), ('B', 'A'), ('C', 'B'), ('A', 'C'), ('A', 'B'),
            ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C'), ('A', 'B'), ('C', 'B'),
            ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C'), ('A', 'B'), ('C', 'B'), ('A', 'C'),
            ('B', 'A'), ('B', 'C'), ('A', 'C')
        ])

if __name__ == "__main__":
    unittest.main()
