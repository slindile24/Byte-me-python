# Placeholder functions for Python basics, to be implemented later

def add_numbers(a, b):
    return a + b

def find_maximum(a, b, c):
    return max(a,b,c)

def is_palindrome(string):
    pass

def count_word_occurrences(text, word):
    pass

def read_file_lines(filepath):
    with open(filepath,'r',errors= 'ignore') as f:
        return f.readlines

def factorial(n):
    pass
#     try:
#         n = int(n)
#     except:
#         raise TypeError("Invalid input type")
#     if n < 0:
#         raise ValueError
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n-1)
# print(factorial(-1))

    

def is_prime(n):
    try:
        n = int(n)
    except:
        raise TypeError("Invalid input type")
    if n < 0:
        raise ValueError
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n %2 == 0:
        return False 
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True
print(is_prime(5))

def sort_numbers(numbers):
    try:
        iter(numbers)
        for element in numbers:
            if not(type(element)==int or type(element)==float):
                raise TypeError("All elements must be numbers")
        return sorted(numbers)
    except:
        raise TypeError("Input must be a number")
        
    # try:
    #     x = int(numbers)
    #     return sorted(x)
    # except:
    #     raise TypeError

def factorial(n):
    if n < 0:
        return ""
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n-1)
print(factorial(-1))

def fibonacci(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
    a,b = 0,1
    
    for i in range(2,n + 1):
        a,b = b,a+b
    return b
    

    # return fibonacci(n-1) + fibonacci(n + 2)



def tower_of_hanoi(n, source, auxiliary, target):
    
    """
    Solve the Tower of Hanoi problem for n disks.

    Args:
        n (int): Number of disks to move.
        source (str): Name of the source peg.
        auxiliary (str): Name of the auxiliary peg.
        target (str): Name of the target peg.

    Returns:
        list: A list of moves to solve the Tower of Hanoi problem.

    Example:
    >>> tower_of_hanoi(3, 'A', 'B', 'C')
    [('A', 'C'), ('A', 'B'), ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C')]
    """
    pass

class Person:
    def __init__(self, name, age):
        pass


if __name__ == "__main__":
    # Placeholder functions for Python basics, to be implemented later
    #to test your functions, you can use the following code
    print(add_numbers(3, 5)) #e.g