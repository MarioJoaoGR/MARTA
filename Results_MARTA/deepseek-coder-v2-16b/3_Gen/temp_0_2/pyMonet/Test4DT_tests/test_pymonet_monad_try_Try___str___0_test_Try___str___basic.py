
import pytest
from pymonet.monad_try import Try  # Assuming this is a hypothetical module

def test_Try___str___basic():
    try_success = Try("result", True)
    assert str(try_success) == 'Try[value=result, is_success=True]'
    
    try_failure = Try('error', False)
    assert str(try_failure) == 'Try[value=error, is_success=False]'
