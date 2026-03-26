# Module: pymonet.monad_try
# test_monad_try.py
from pymonet.monad_try import Try

def test_successful_try():
    successful_try = Try(42, is_success=True)
    assert successful_try.is_success == True
    assert successful_try.value == 42

def test_failed_try():
    failed_try = Try("Operation failed", is_success=False)
    assert failed_try.is_success == False
    assert failed_try.value == "Operation failed"

def test_map_successful_try():
    successful_try = Try(42, is_success=True)
    mapped_try = successful_try.map(lambda x: x * 2)
    assert mapped_try.is_success == True
    assert mapped_try.value == 84

def test_map_failed_try():
    failed_try = Try("Operation failed", is_success=False)
    mapped_try = failed_try.map(lambda x: x * 2)
    assert mapped_try.is_success == False
    assert mapped_try.value == "Operation failed"

def test_map_with_function():
    successful_try = Try(42, is_success=True)
    def double(x):
        return x * 2
    mapped_try = successful_try.map(double)
    assert mapped_try.is_success == True
    assert mapped_try.value == 84

def test_map_with_failing_function():
    failed_try = Try("Operation failed", is_success=False)
    def failing_function(x):
        raise ValueError("Operation failed")
    try_with_failing_map = failed_try.map(failing_function)
    assert try_with_failing_map.is_success == False
    assert try_with_failing_map.value == "Operation failed"
