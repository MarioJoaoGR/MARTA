
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_none_input():
    with pytest.raises(InvalidInputError):
        formatter = __StringFormatter(None)
