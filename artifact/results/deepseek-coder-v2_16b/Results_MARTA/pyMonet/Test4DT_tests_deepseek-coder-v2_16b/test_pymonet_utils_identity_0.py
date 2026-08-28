
import pytest
from pymonet.utils import identity

def test_identity_with_int():
    result = identity(5)
    assert result == 5, f"Expected 5 but got {result}"

def test_identity_with_str():
    result = identity("hello")
    assert result == "hello", f"Expected 'hello' but got {result}"

def test_identity_with_list():
    result = identity([1, 2, 3])
    assert result == [1, 2, 3], f"Expected [1, 2, 3] but got {result}"

def test_error_handling_invalid_type():
    with pytest.raises(TypeError):
        identity()
