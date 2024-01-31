# File: test_math_operations.py

def add_numbers(a, b):
    return a + b

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(10, -5) == 5

if __name__ == "__main__":
    # Run the tests if the script is executed
    test_add_numbers()
