
# Module: string_utils.manipulation
# Import the function from its module
from string_utils.manipulation import prettify
import pytest

# Test cases for the prettify function
def test_typical_usage():
    input_string = 'unprettified string ,, like this one,will be"prettified" .it\\\' s awesome!'
    expected_output = 'Unprettified string, like this one, will be "prettified". It\'s awesome!'
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

python-string-utils/Test4DT_tests/test_string_utils_manipulation_prettify_0.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
______________________________ test_typical_usage ______________________________

    def test_typical_usage():
        input_string = 'unprettified string ,, like this one,will be"prettified" .it\\\' s awesome!'
        expected_output = 'Unprettified string, like this one, will be "prettified". It\'s awesome!'
>       assert prettify(input_string) == expected_output
E       assert "Unprettified...\' s awesome!" == "Unprettified...It's awesome!"
E         
E         Skipping 50 identical leading characters in diff, use -v to show
E         - ified". It's awesome!
E         + ified". It\' s awesome!
E         ?           + +

python-string-utils/Test4DT_tests/test_string_utils_manipulation_prettify_0.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation_prettify_0.py::test_typical_usage
========================= 1 failed, 1 passed in 0.03s ==========================

"""