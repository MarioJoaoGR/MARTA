
from string_utils.manipulation import snake_case_to_camel

def test_valid_case():
    # Test with a valid snake case input
    assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    
    # Test without uppercasing the first letter
    assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    
    # Test with a different separator
    assert snake_case_to_camel('the-snake-is-green', separator='-') == 'TheSnakeIsGreen'
    
    # Test with an invalid snake case input (unchanged)
    assert snake_case_to_camel('invalid_input') == 'invalid_input'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation_snake_case_to_camel_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        # Test with a valid snake case input
        assert snake_case_to_camel('the_snake_is_green') == 'TheSnakeIsGreen'
    
        # Test without uppercasing the first letter
        assert snake_case_to_camel('the_snake_is_green', upper_case_first=False) == 'theSnakeIsGreen'
    
        # Test with a different separator
        assert snake_case_to_camel('the-snake-is-green', separator='-') == 'TheSnakeIsGreen'
    
        # Test with an invalid snake case input (unchanged)
>       assert snake_case_to_camel('invalid_input') == 'invalid_input'
E       AssertionError: assert 'InvalidInput' == 'invalid_input'
E         
E         - invalid_input
E         ? ^      ^^
E         + InvalidInput
E         ? ^      ^

python-string-utils/Test4DT_tests/test_string_utils_manipulation_snake_case_to_camel_0_test_valid_case.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation_snake_case_to_camel_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.02s ===============================
"""