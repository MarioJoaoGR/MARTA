
import pytest
from pymonet.monad_try import Try

def test_map_with_success():
    successful_try = Try(42, is_success=True)
    mapped_try = successful_try.map(lambda x: x * 2)
    
    assert mapped_try.is_success == True
    assert mapped_try.value == 84

def test_map_with_failure():
    failed_try = Try("Operation failed", is_success=False)
    mapped_try = failed_try.map(lambda x: x * 2)
    
    assert mapped_try.is_success == False
    assert mapped_try.value == "Operation failed"

def test_map_with_none():
    try_with_none = Try(None, is_success=True)
    mapped_try = try_with_none.map(lambda x: x * 2 if x is not None else None)
    
    assert mapped_try.is_success == True
    assert mapped_try.value is None

def test_map_with_empty_list():
    empty_list_try = Try([], is_success=True)
    mapped_try = empty_list_try.map(lambda x: x + [1])
    
    assert mapped_try.is_success == True
    assert mapped_try.value == [1]
