
import re
from string_utils.validation import is_uuid
import pytest

# Assuming UUID_RE and UUID_HEX_OK_RE are defined in the module 'string_utils.validation'
UUID_RE = re.compile(r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$')
UUID_HEX_OK_RE = re.compile(r'^[0-9a-fA-F]+$')

def test_invalid_uuid():
    assert not is_uuid('invalid-uuid')  # This should fail because it's an invalid UUID format
    assert not is_uuid('6f8aa2f9686c4ac387665712354a04cf', allow_hex=True)  # This should also fail because it's not a valid standard UUID format

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_uuid_1_test_invalid_uuid.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_uuid _______________________________

    def test_invalid_uuid():
        assert not is_uuid('invalid-uuid')  # This should fail because it's an invalid UUID format
>       assert not is_uuid('6f8aa2f9686c4ac387665712354a04cf', allow_hex=True)  # This should also fail because it's not a valid standard UUID format
E       AssertionError: assert not True
E        +  where True = is_uuid('6f8aa2f9686c4ac387665712354a04cf', allow_hex=True)

python-string-utils/Test4DT_tests/test_string_utils_validation_is_uuid_1_test_invalid_uuid.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_uuid_1_test_invalid_uuid.py::test_invalid_uuid
============================== 1 failed in 0.03s ===============================
"""