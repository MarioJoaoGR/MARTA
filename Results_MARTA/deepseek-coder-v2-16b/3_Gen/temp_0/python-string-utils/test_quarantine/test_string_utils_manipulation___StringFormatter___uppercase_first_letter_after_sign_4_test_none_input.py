
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def is_string(value):
    return isinstance(value, str)

class Test__StringFormatter:
    
    def test_none_input(self):
        with pytest.raises(InvalidInputError) as excinfo:
            formatter = __StringFormatter(None)
        assert "Expected 'str', received 'NoneType'" in str(excinfo.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___uppercase_first_letter_after_sign_4_test_none_input.py F [100%]

=================================== FAILURES ===================================
____________________ Test__StringFormatter.test_none_input _____________________

self = <Test4DT_tests.test_string_utils_manipulation___StringFormatter___uppercase_first_letter_after_sign_4_test_none_input.Test__StringFormatter object at 0x1032ad840>

    def test_none_input(self):
        with pytest.raises(InvalidInputError) as excinfo:
>           formatter = __StringFormatter(None)
E           NameError: name '_Test__StringFormatter__StringFormatter' is not defined

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___uppercase_first_letter_after_sign_4_test_none_input.py:12: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___uppercase_first_letter_after_sign_4_test_none_input.py::Test__StringFormatter::test_none_input
============================== 1 failed in 0.03s ===============================
"""