
import re
from string_utils.validation import words_count

def test_valid_case_happy_path():
    # Test with a simple string containing multiple words
    assert words_count('hello world') == 2
    
    # Test with a string containing punctuation and spaces
    assert words_count('one,two,three.stop') == 4
    
    # Test with a string containing only letters and numbers
    assert words_count('Python3.8 is awesome!') == 2

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_words_count_0_test_valid_case_happy_path.py F [100%]

=================================== FAILURES ===================================
__________________________ test_valid_case_happy_path __________________________

    def test_valid_case_happy_path():
        # Test with a simple string containing multiple words
        assert words_count('hello world') == 2
    
        # Test with a string containing punctuation and spaces
        assert words_count('one,two,three.stop') == 4
    
        # Test with a string containing only letters and numbers
>       assert words_count('Python3.8 is awesome!') == 2
E       AssertionError: assert 4 == 2
E        +  where 4 = words_count('Python3.8 is awesome!')

python-string-utils/Test4DT_tests/test_string_utils_validation_words_count_0_test_valid_case_happy_path.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_words_count_0_test_valid_case_happy_path.py::test_valid_case_happy_path
============================== 1 failed in 0.03s ===============================
"""