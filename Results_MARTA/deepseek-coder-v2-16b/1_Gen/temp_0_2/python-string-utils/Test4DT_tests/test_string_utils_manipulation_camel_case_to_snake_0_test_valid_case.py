
import re
from string_utils.manipulation import camel_case_to_snake, is_camel_case, is_string
from string_utils.errors import InvalidInputError

def test_valid_case():
    # Test case where the input string is in camel case format
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'
    
    # Additional test cases to ensure robustness
    assert camel_case_to_snake('anotherCamelCaseExample') == 'another_camel_case_example'
    assert camel_case_to_snake('oneMoreTestCase') == 'one_more_test_case'
    assert camel_case_to_snake('allLowercaseInput') == 'all_lowercase_input'
    # Should not be converted if not camel case
    assert camel_case_to_snake('ALLUPPERCASEINPUT') == 'ALLUPPERCASEINPUT'
