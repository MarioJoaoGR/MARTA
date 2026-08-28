
# Module: pymonet.monad_try
# test_monad_try.py
from pymonet.monad_try import Try

def test_successful_try():
    # Test creating a successful Try instance
    success = Try(42, True)
    assert success.value == 42
    assert success.is_success is True

def test_failed_try():
    # Test creating a failed Try instance
    failure = Try("error", False)
    assert failure.is_success is False
    assert failure.value == "error"

def test_on_success_callback():
    # Test using the on_success method with a callback function
    success = Try(42, True)
    
    def print_value(val):
        assert val == 42
    
    result = success.on_success(print_value)
    assert result.value == 42

def test_on_fail_callback():
    # Test using the on_fail method with a callback function
    failure = Try("error", False)
    
    def print_error(val):
        assert val == "error"
    
    result = failure.on_success(print_error)
    assert result.value == "error"

def test_map_method():
    # Test using the map method to transform the value if successful
    success = Try(42, True)
    
    def square(x): return x * x
    
    transformed = success.map(square)
    assert transformed.value == 1764

def test_bind_method():
    # Test using the bind method to apply a function that might fail
    success = Try(10, True)
    
    def add_ten(x): return x + 10
    
    result = success.bind(add_ten)