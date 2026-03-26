
import re
from string_utils.manipulation import camel_case_to_snake

def is_string(input_string):
    return isinstance(input_string, str)

def is_camel_case(input_string):
    return bool(re.search(r'^[a-z]+([A-Z][a-z]*)*$', input_string))

class InvalidInputError(Exception):
    pass

CAMEL_CASE_REPLACE_RE = re.compile(r'(?<!^)(?=[A-Z])')

def test_valid_case():
    # Test case where the input string is in camel case format
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'
    
    # Additional test cases to ensure robustness
    assert camel_case_to_snake('anotherCamelCaseExample') == 'another_camel_case_example'
    assert camel_case_to_snake('oneMoreTestCase') == 'one_more_test_case'
    assert camel_case_to_snake('allLowercaseInput') == 'all_lowercase_input'
    assert camel_case_to_snake('ALLUPPERCASEINPUT') == 'alluppercaseinput'  # Should not be converted if not camel case

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation_camel_case_to_snake_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        # Test case where the input string is in camel case format
        assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'
    
        # Additional test cases to ensure robustness
        assert camel_case_to_snake('anotherCamelCaseExample') == 'another_camel_case_example'
        assert camel_case_to_snake('oneMoreTestCase') == 'one_more_test_case'
        assert camel_case_to_snake('allLowercaseInput') == 'all_lowercase_input'
>       assert camel_case_to_snake('ALLUPPERCASEINPUT') == 'alluppercaseinput'  # Should not be converted if not camel case
E       AssertionError: assert 'ALLUPPERCASEINPUT' == 'alluppercaseinput'
E         
E         - alluppercaseinput
E         + ALLUPPERCASEINPUT

python-string-utils/Test4DT_tests/test_string_utils_manipulation_camel_case_to_snake_0_test_valid_case.py:24: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation_camel_case_to_snake_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.03s ===============================
"""