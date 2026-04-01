
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_error_case():
    with pytest.raises(InvalidInputError) as exc_info:
        formatter = __StringFormatter(12345)
    
    assert isinstance(exc_info.value, InvalidInputError)
    assert exc_info.value.args[0] == 'Expected "str", received "int"'
