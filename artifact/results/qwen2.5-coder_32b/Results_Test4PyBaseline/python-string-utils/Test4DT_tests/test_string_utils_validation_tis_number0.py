
from string_utils import is_number

def test_is_number_scientific_notation():
    assert is_number('1e3') == True