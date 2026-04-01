
import pytest
from string_utils.manipulation import snake_case_to_camel

def test_edge_case():
    # Test case where input is an empty string
    assert snake_case_to_camel('') == ''
    
    # Test case where input is not a valid snake case string
    assert snake_case_to_camel('invalid-snake_case') == 'invalid-snake_case'
    
    # Test case where input is a valid snake case string with uppercase first letter
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=True) == 'TheSnakeIsGreen'
    
    # Test case where input is a valid snake case string with lowercase first letter
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    
    # Test case where input contains only one word
    assert snake_case_to_camel('onlyoneword') == 'onlyoneword'
