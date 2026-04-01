
import pytest
from string_utils.validation import words_count, InvalidInputError

def test_valid_input_one_two_three_stop():
    input_string = "one,two,three.stop"
    expected_count = 4
    
    assert words_count(input_string) == expected_count
