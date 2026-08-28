
from string_utils import snake_case_to_camel

def test_snake_case_to_camel_single_word_upper_case_first():
    assert snake_case_to_camel('singleword', upper_case_first=True) == 'singleword'
    assert snake_case_to_camel('singleword', upper_case_first=False) == 'singleword'
