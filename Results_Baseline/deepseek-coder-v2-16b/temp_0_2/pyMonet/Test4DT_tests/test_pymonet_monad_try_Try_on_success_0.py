
# Module: pymonet.monad_try
# test_monad_try.py
from pymonet.monad_try import Try

def test_successful_try_instance():
    try_instance = Try(42, True)  # Creates a Try instance with value 42 and success status set to True.
    assert try_instance.value == 42
    assert try_instance.is_success is True

def test_failed_try_instance():
    try_failure = Try("example", False)  # Creates a Try instance with value "example" and success status set to False.
    assert try_failure.value == "example"
    assert try_failure.is_success is False

def test_on_success_method():
    def print_success(x):
        assert x == 42
    
    try_instance = Try(42, True)
    result = try_instance.on_success(print_success)
    assert result is try_instance

def test_on_fail_method():
    def print_error(value):
        assert value == "example"
    
    try_failure = Try("example", False)
    result = try_failure.on_fail(print_error)
    assert result is try_failure

def test_map_method():
    def square(x):
        return x * x
    
    try_instance = Try(3, True)
    mapped_try = try_instance.map(square)  # Creates a new Try instance with the value 9 (since 3^2 is 9).
    assert mapped_try.value == 9

def test_bind_method():
    def square(x):
        return Try(x * x, True) if isinstance(x, int) and x >= 0 else Try("error", False)
    
    try_instance = Try(3, True)
    result = try_instance.bind(square)  # result will be Try with value 9 (since 3^2 is 9).
    assert isinstance(result, Try) and result.value == 9

def test_on_success_callback():
    def print_success(x):
        print("Success:", x)
    
    try_instance = Try(42, True)
    try_instance.on_success(print_success)  # Outputs: Success: 42

def test_on_fail_callback():
    def print_error(value):
        print(f"Error: {value}")
    
    try_instance = Try("some error", False)
    try_instance.on_fail(print_error)  # Outputs: Error: some error
