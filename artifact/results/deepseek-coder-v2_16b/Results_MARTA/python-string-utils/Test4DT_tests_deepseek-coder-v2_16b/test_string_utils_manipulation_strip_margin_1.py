
import pytest
from string_utils.manipulation import strip_margin

def is_string(obj):
    return isinstance(obj, str)

class InvalidInputError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Expected "str", received "{type(self.value).__name__}"'



def test_edge_case_single_line():
    input_string = '    line 1'
    expected_output = 'line 1'
    assert strip_margin(input_string) == expected_output
