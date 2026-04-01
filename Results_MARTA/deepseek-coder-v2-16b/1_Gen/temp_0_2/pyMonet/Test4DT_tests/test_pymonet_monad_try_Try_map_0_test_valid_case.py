
import pytest
from pymonet.monad_try import Try

def test_valid_case():
    success = Try(5, True)
    mapped_success = success.map(lambda x: x * x)
    
    assert mapped_success.value == 25
    assert mapped_success.is_success is True
