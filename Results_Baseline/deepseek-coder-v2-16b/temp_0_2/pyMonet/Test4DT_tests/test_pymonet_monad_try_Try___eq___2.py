
# Module: pymonet.monad_try
# test_monad_try.py
from pymonet.monad_try import Try

def test_successful_creation():
    try_instance = Try(42, True)
    assert try_instance.value == 42
    assert try_instance.is_success is True

def test_failed_creation():
    try_failure = Try("example", False)
    assert try_failure.value == "example"
    assert try_failure.is_success is False

def test_map_method():
    def square(x):
        return x * x
    
    try_instance = Try(3, True)
    mapped_try = try_instance.map(square)
    assert mapped_try.value == 9
    assert mapped_try.is_success is True

def test_bind_method():
    def square(x):
        if isinstance(x, int) and x > 0:
            return Try(x * x, True)
        else:
            return Try(None, False)
    
    try_instance = Try(3, True)
    result = try_instance.bind(square)
    assert isinstance(result, Try)
    if result.is_success:
        assert result.value == 9
    else:
        assert False, "Expected success but got failure"

def test_eq_method():
    # Test equality with another Try instance of the same type, value, and success status
    try1 = Try(42, True)
    try2 = Try(42, True)
    assert try1 == try2  # Should be true since all properties are equal

def test_eq_method_different_type():
    # Test equality with an instance of a different class
    try1 = Try(42, True)
    maybe_instance = Try(42, False)  # A Maybe instance with the same value but different success status
    assert not (try1 == maybe_instance)  # Should be false since types are different

def test_eq_method_different_value():
    # Test equality with another Try instance of the same type but different value
    try1 = Try(42, True)
    try2 = Try(99, True)
    assert not (try1 == try2)  # Should be false since values are different

def test_eq_method_different_success():
    # Test equality with another Try instance of the same type but different success status
    try1 = Try(42, True)
    try2 = Try(42, False)
    assert not (try1 == try2)  # Should be false since success status is different
