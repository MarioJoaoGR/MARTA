
import re
from string_utils.validation import is_slug

def test_empty_string():
    assert not is_slug('')
    assert not is_slug(' ')
    assert not is_slug('  ')
    assert not is_slug('abc')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_slug_2_test_empty_string.py F [100%]

=================================== FAILURES ===================================
______________________________ test_empty_string _______________________________

    def test_empty_string():
        assert not is_slug('')
        assert not is_slug(' ')
        assert not is_slug('  ')
>       assert not is_slug('abc')
E       AssertionError: assert not True
E        +  where True = is_slug('abc')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_slug_2_test_empty_string.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_slug_2_test_empty_string.py::test_empty_string
============================== 1 failed in 0.03s ===============================
"""