
from unittest.mock import patch
import uuid as py_uuid

def uuid(as_hex: bool = False) -> str:
    """
    Generates a universally unique identifier (UUID) which is represented as a string. By default, the UUID is returned in its standard format. If the parameter `as_hex` is set to True, the function returns the hexadecimal representation of the UUID.

    The function uses `uuid.uuid4()` to generate the UUID and can switch between the standard format and the hex value based on the `as_hex` parameter.

    *Examples:*

    >>> uuid() # possible output: '97e3a716-6b33-4ab9-9bb1-8128cb24d76b'
    >>> uuid(as_hex=True) # possible output: '97e3a7166b334ab99bb18128cb24d76b'

    :param as_hex: A boolean flag to determine the format of the UUID string. If True, returns the hex value; if False (default), returns the standard UUID representation.
    :return: A string representing the UUID. If `as_hex` is True, it returns the hexadecimal representation; otherwise, it returns the default UUID string format.
    """
    uid = py_uuid.uuid4()

    if as_hex:
        return uid.hex

    return str(uid)

# Test case for valid input hex format
def test_valid_input_hex_format():
    with patch('string_utils.generation.uuid', side_effect=lambda: py_uuid.UUID('97e3a716-6b33-4ab9-9bb1-8128cb24d76b')):
        assert uuid(as_hex=True) == '97e3a7166b334ab99bb18128cb24d76b'
        assert uuid() != '97e3a7166b334ab99bb18128cb24d76b'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_generation_uuid_1_test_valid_input_hex_format.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_hex_format __________________________

    def test_valid_input_hex_format():
        with patch('string_utils.generation.uuid', side_effect=lambda: py_uuid.UUID('97e3a716-6b33-4ab9-9bb1-8128cb24d76b')):
>           assert uuid(as_hex=True) == '97e3a7166b334ab99bb18128cb24d76b'
E           AssertionError: assert '64190e9ea97a...9751f6326b3db' == '97e3a7166b33...18128cb24d76b'
E             
E             - 97e3a7166b334ab99bb18128cb24d76b
E             + 64190e9ea97a45ca9aa9751f6326b3db

python-string-utils/Test4DT_tests/test_string_utils_generation_uuid_1_test_valid_input_hex_format.py:29: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_generation_uuid_1_test_valid_input_hex_format.py::test_valid_input_hex_format
============================== 1 failed in 0.03s ===============================

"""