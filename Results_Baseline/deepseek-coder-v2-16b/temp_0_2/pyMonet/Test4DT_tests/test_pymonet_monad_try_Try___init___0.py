
# Module: pymonet.monad_try
from pymonet.monad_try import Try

def test_successful_try_instance():
    try_instance = Try(42, True)  # Creates a Try instance with value 42 and success status set to True.
    assert try_instance.value == 42
    assert try_instance.is_success is True

def test_failed_try_instance():
    try_failure = Try("example", False)  # Creates a Try instance with value "example" and success status set to False.
    assert try_failure.value == "example"
    assert try_failure.is_success is False

def test_map_method():
    def square(x):
        return x * x
    
    try_instance = Try(3, True)
    mapped_try = try_instance.map(square)  # Creates a new Try instance with the value 9 (since 3^2 is 9).
    assert mapped_try.value == 9

def test_bind_method():
    def square(x):
        return Try(x * x, True) if isinstance(x, int) and x >= 0 else Try(None, False)
    
    try_instance = Try(3, True)
    result = try_instance.bind(square)  # result will be Try with value 9 (since 3^2 is 9).
    assert result.value == 9
    assert result.is_success is True

def test_on_success_method():
    def print_success(x):
        print("Success:", x)
    
    try_instance = Try(42, True)
    try_instance.on_success(print_success)  # Outputs: Success: 42

def test_on_fail_method():
    def print_error(value):
        print(f"Error: {value}")
    
    try_instance = Try("some error", False)
    try_instance.on_fail(print_error)  # Outputs: Error: some error

def test_filter_method():
    def is_even(n):
        return n % 2 == 0
    
    try_instance = Try(42, True)
    filtered_try = try_instance.filter(is_even)  # Filtered_try will have the same value and success status as try_instance because 42 is even.
    assert filtered_try.value == 42
    assert filtered_try.is_success is True

def test_get_method():
    try_instance = Try(42, True)
    result = try_instance.get()  # This will return the encapsulated value if is_success is True.
    assert result == 42

def test_get_or_else_method():
    try_instance = Try("some error", False)
    result = try_instance.get_or_else(0)  # This will return the encapsulated value if is_success is True, otherwise 0.
    assert result == 0
