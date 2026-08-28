
import re
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError



def test_invalid_input_non_string():
    with pytest.raises(InvalidInputError) as excinfo:
        __StringFormatter(123)
    assert str(excinfo.value) == 'Expected "str", received "int"'

