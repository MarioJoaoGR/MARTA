
import pytest
from string_utils.validation import is_ip_v4, is_full_string, SHALLOW_IP_V4_RE

@pytest.mark.parametrize("input_value", [None, "", "   ", "192.168.1.1"])
def test_invalid_input_none(input_value):
    assert not is_ip_v4(input_value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_v4_6_test_invalid_input_none.py . [ 25%]
..F                                                                      [100%]

=================================== FAILURES ===================================
_____________________ test_invalid_input_none[192.168.1.1] _____________________

input_value = '192.168.1.1'

    @pytest.mark.parametrize("input_value", [None, "", "   ", "192.168.1.1"])
    def test_invalid_input_none(input_value):
>       assert not is_ip_v4(input_value)
E       AssertionError: assert not True
E        +  where True = is_ip_v4('192.168.1.1')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_v4_6_test_invalid_input_none.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_v4_6_test_invalid_input_none.py::test_invalid_input_none[192.168.1.1]
========================= 1 failed, 3 passed in 0.04s ==========================
"""