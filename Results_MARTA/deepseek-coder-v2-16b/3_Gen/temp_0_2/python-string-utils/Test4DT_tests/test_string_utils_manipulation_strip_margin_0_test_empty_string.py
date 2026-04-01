
import re
from string_utils.manipulation import strip_margin, InvalidInputError

def test_empty_string():
    input_string = ""
    expected_output = ""
    assert strip_margin(input_string) == expected_output
