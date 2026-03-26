
import pytest
from string_utils.manipulation import __StringFormatter

@pytest.fixture(scope="module")
def valid_formatter():
    return __StringFormatter("hello world")

def test_remove_duplicates(valid_formatter):
    # Assuming the method expects a regex match object to extract the first character of the matched group
    # We need to mock or provide an appropriate regex match object for this test
    
    # Create a mock regex match object with a sample group value
    class MockMatch:
        def __init__(self, group):
            self.group = lambda _: group
    
    # Provide a valid input string that has duplicates to ensure the method can handle it
    valid_input_string = "helloo world"
    
    # Call the method with the mock match object and the valid input string
    result = valid_formatter._StringFormatter__remove_duplicates(valid_input_string, regex_match=MockMatch("hello"))
    
    # Assert that the result is as expected after removing duplicates
    assert result == "he"  # Expected output after removing duplicates based on the first character of the matched group

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___remove_duplicates_4_test_valid_input.py F [100%]

=================================== FAILURES ===================================
____________________________ test_remove_duplicates ____________________________

valid_formatter = <string_utils.manipulation.__StringFormatter object at 0x1062560e0>

    def test_remove_duplicates(valid_formatter):
        # Assuming the method expects a regex match object to extract the first character of the matched group
        # We need to mock or provide an appropriate regex match object for this test
    
        # Create a mock regex match object with a sample group value
        class MockMatch:
            def __init__(self, group):
                self.group = lambda _: group
    
        # Provide a valid input string that has duplicates to ensure the method can handle it
        valid_input_string = "helloo world"
    
        # Call the method with the mock match object and the valid input string
>       result = valid_formatter._StringFormatter__remove_duplicates(valid_input_string, regex_match=MockMatch("hello"))
E       TypeError: __StringFormatter.__remove_duplicates() got multiple values for argument 'regex_match'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___remove_duplicates_4_test_valid_input.py:22: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___remove_duplicates_4_test_valid_input.py::test_remove_duplicates
============================== 1 failed in 0.04s ===============================
"""