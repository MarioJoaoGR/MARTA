
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
        return x * x
    
    try_instance = Try(3, True)
    result = try_instance.bind(square)