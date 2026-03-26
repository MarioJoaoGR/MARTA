
import re
from string_utils.manipulation import camel_case_to_snake, is_string, is_camel_case
from unittest.mock import patch

def test_valid_camel_to_snake():
    input_string = 'ThisIsACamelStringTest'
    expected_output = 'this_is_a_camel_string_test'
    
    with patch('string_utils.manipulation.is_camel_case') as mock_is_camel_case:
        mock_is_camel_case.return_value = True
        
        result = camel_case_to_snake(input_string)
        
        assert result == expected_output
