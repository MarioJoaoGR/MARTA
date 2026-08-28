
# Import the snake_case_to_camel function from the string_utils module
from string_utils import snake_case_to_camel

def test_snake_case_to_camel_single_word():
    assert snake_case_to_camel('singleword') == 'singleword'
    assert snake_case_to_camel('singleword', upper_case_first=False) == 'singleword'
