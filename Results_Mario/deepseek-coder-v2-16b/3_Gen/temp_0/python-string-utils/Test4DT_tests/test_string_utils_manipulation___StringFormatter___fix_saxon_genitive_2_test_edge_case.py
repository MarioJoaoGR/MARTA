
from string_utils.manipulation import __StringFormatter, InvalidInputError
import re

def test_edge_case():
    # Test with a valid string input
    formatter = __StringFormatter("valid string")
    assert formatter.input_string == "valid string"
    
    # Test with an invalid type (int) to raise InvalidInputError
    try:
        bad_formatter = __StringFormatter(12345)
    except InvalidInputError as e:
        assert str(e) == 'Expected "str", received "int"'
