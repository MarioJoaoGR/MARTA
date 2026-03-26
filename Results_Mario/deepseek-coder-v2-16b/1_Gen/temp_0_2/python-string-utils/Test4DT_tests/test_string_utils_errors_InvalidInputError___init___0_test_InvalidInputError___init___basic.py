
import pytest
from string_utils.errors import InvalidInputError

def test_InvalidInputError___init___basic():
    with pytest.raises(InvalidInputError) as excinfo:
        raise InvalidInputError("not a string")
    assert str(excinfo.value) == 'Expected "str", received "str"'
