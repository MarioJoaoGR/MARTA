
import re
from string_utils.validation import InvalidInputError, words_count

def test_valid_input():
    assert words_count('hello world') == 2
    assert words_count('one,two,three.stop') == 4
    assert words_count('Python! is great.') == 3
    assert words_count('123-456-7890') == 1

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_words_count_1_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        assert words_count('hello world') == 2
        assert words_count('one,two,three.stop') == 4
        assert words_count('Python! is great.') == 3
>       assert words_count('123-456-7890') == 1
E       AssertionError: assert 3 == 1
E        +  where 3 = words_count('123-456-7890')

python-string-utils/Test4DT_tests/test_string_utils_validation_words_count_1_test_valid_input.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_words_count_1_test_valid_input.py::test_valid_input
============================== 1 failed in 0.03s ===============================
"""