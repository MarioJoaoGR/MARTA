
import pytest
from string_utils.manipulation import snake_case_to_camel

def test_edge_case():
    # Test case where input is an empty string
    assert snake_case_to_camel('') == ''
    
    # Test case where input is not a valid snake case string
    assert snake_case_to_camel('invalid-snake_case') == 'invalid-snake_case'
    
    # Test case where input is a valid snake case string and upper_case_first is False
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    
    # Test case where input is a valid snake case string and upper_case_first is True (default)
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
