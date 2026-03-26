
# Module: pymonet.monad_try
# test_monad_try.py
from pymonet.monad_try import Try

def test_successful_creation():
    successful_try = Try(42, is_success=True)
    assert successful_try.is_success == True
    assert successful_try.value == 42

def test_failed_creation():
    failed_try = Try("Operation failed", is_success=False)
    assert failed_try.is_success == False
    assert failed_try.value == "Operation failed"

def test_filter_with_even_number():
    even_try = Try(4, is_success=True)
    filtered_even_try = even_try.filter(lambda n: n % 2 == 0)
    assert filtered_even_try.is_success == True
    assert filtered_even_try.value == 4

def test_filter_with_odd_number():
    odd_try = Try(3, is_success=True)
    filtered_odd_try = odd_try.filter(lambda n: n % 2 == 0)
    assert filtered_odd_try.is_success == False
    assert filtered_odd_try.value == 3

def test_map_transformation():
    try_with_square = Try(5, is_success=True)
    mapped_try = try_with_square.map(lambda n: n * n)
    assert mapped_try.is_success == True
    assert mapped_try.value == 25

def test_bind_chaining():
    def add_one(n):
        return Try(n + 1, is_success=True)
    
    try_with_add_one = Try(4, is_success=True)
    bound_try = try_with_add_one.bind(add_one)
    assert bound_try.is_success == True
    assert bound_try.value == 5

def test_handle_success():
    def handle_success(value):
        assert value == 42
    
    successful_try = Try(42, is_success=True)
    successful_try.on_success(handle_success)

def test_handle_failure():
    def handle_failure(error):
        assert error == "Operation failed"
    
    failed_try = Try("Operation failed", is_success=False)
    failed_try.on_fail(handle_failure)
