
import pytest
from string_utils.manipulation import booleanize, InvalidInputError

def test_booleanize_basic():
    # Test positive cases returning True
    assert booleanize('true') is True
    assert booleanize('YES') is True
    assert booleanize('1') is True
    assert booleanize('y') is True

    # Test negative case returning False
    assert booleanize('nope') is False
    assert booleanize('false') is False
    assert booleanize('0') is False
    assert booleanize('n') is False

    # Test edge cases with different casing
    assert booleanize('TrUe') is True
    assert booleanize('YeS') is True

    # Test invalid input type raises InvalidInputError
    with pytest.raises(InvalidInputError):
        booleanize(123)
