
import pytest
from string_utils.manipulation import snake_case_to_camel

def test_snake_case_to_camel_edge_cases():
    # Test with an empty string
    assert snake_case_to_camel('') == ''
    
    # Test with a non-snake case string
    assert snake_case_to_camel('thisIsCamelCase') == 'thisIsCamelCase'
    
    # Test with a valid snake case string, upper_case_first=True
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=True) == 'TheSnakeIsGreen'
    
    # Test with a valid snake case string, upper_case_first=False
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    
    # Test with a valid snake case string and custom separator
    assert snake_case_to_camel('the-snake-is-green', separator='-') == 'TheSnakeIsGreen'
    
    # Test with an invalid snake case string
    assert snake_case_to_camel('invalid_snake_case_string') == 'invalid_snake_case_string'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation_snake_case_to_camel_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
_____________________ test_snake_case_to_camel_edge_cases ______________________

    def test_snake_case_to_camel_edge_cases():
        # Test with an empty string
        assert snake_case_to_camel('') == ''
    
        # Test with a non-snake case string
        assert snake_case_to_camel('thisIsCamelCase') == 'thisIsCamelCase'
    
        # Test with a valid snake case string, upper_case_first=True
        assert snake_case_to_camel('the_snake_is_green', upper_case_first=True) == 'TheSnakeIsGreen'
    
        # Test with a valid snake case string, upper_case_first=False
        assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    
        # Test with a valid snake case string and custom separator
        assert snake_case_to_camel('the-snake-is-green', separator='-') == 'TheSnakeIsGreen'
    
        # Test with an invalid snake case string
>       assert snake_case_to_camel('invalid_snake_case_string') == 'invalid_snake_case_string'
E       AssertionError: assert 'InvalidSnakeCaseString' == 'invalid_snake_case_string'
E         
E         - invalid_snake_case_string
E         ? ^      ^^    ^^   ^^
E         + InvalidSnakeCaseString
E         ? ^      ^    ^   ^

python-string-utils/Test4DT_tests/test_string_utils_manipulation_snake_case_to_camel_0_test_edge_case.py:22: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation_snake_case_to_camel_0_test_edge_case.py::test_snake_case_to_camel_edge_cases
============================== 1 failed in 0.03s ===============================
"""