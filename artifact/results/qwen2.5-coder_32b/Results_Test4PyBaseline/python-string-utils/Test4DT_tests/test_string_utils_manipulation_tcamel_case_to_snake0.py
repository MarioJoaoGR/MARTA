
from string_utils import camel_case_to_snake

def test_camel_case_to_snake_single_uppercase_letter():
    assert camel_case_to_snake('A') == 'A'
