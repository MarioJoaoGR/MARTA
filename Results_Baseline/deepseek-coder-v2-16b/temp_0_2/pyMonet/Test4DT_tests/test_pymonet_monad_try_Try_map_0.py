# Module: pymonet.monad_try
# test_monad_try.py
from pymonet.monad_try import Try

def test_init():
    # Test initialization with success
    try_instance = Try(42, True)
    assert try_instance.value == 42
    assert try_instance.is_success is True

    # Test initialization with failure
    try_failure = Try("example", False)
    assert try_failure.value == "example"
    assert try_failure.is_success is False

def test_map():
    def square(x):
        return x * x
    
    # Test map with success
    try_instance = Try(3, True)
    mapped_try = try_instance.map(square)
    assert mapped_try.value == 9
    assert mapped_try.is_success is True
    
    # Test map with failure
    failed_try = Try("example", False)
    mapped_failed_try = failed_try.map(square)
    assert mapped_failed_try.value == "example"
    assert mapped_failed_try.is_success is False

def test_map_with_failure():
    def square(x):
        return x * x
    
    try_instance = Try("error", False)
    mapped_try = try_instance.map(square)
    assert mapped_try.value == "error"
    assert mapped_try.is_success is False
