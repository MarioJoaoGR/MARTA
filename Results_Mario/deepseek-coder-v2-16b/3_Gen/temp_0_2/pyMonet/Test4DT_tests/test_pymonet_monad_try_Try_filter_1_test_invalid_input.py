
import pytest
from pymonet.monad_try import Try

def test_invalid_input():
    try_object = Try('failure', True)
    filterer_func = lambda x: False
    result = try_object.filter(filterer_func)
    assert not result.is_success
    assert result.value == 'failure'
