
import pytest
from unittest.mock import patch
from uuid import uuid4
from string_utils.generation import uuid

@pytest.mark.parametrize("as_hex, expected", [
    (False, '97e3a716-6b33-4ab9-9bb1-8128cb24d76b'),
    (True, '97e3a7166b334ab99bb18128cb24d76b')
])
def test_valid_input_hex_format(as_hex, expected):
    with patch('string_utils.generation.uuid4', return_value='mocked_uuid'):
        result = uuid(as_hex)
        assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

python-string-utils/Test4DT_tests/test_string_utils_generation_uuid_0_test_valid_input_hex_format.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
___ test_valid_input_hex_format[False-97e3a716-6b33-4ab9-9bb1-8128cb24d76b] ____

as_hex = False, expected = '97e3a716-6b33-4ab9-9bb1-8128cb24d76b'

    @pytest.mark.parametrize("as_hex, expected", [
        (False, '97e3a716-6b33-4ab9-9bb1-8128cb24d76b'),
        (True, '97e3a7166b334ab99bb18128cb24d76b')
    ])
    def test_valid_input_hex_format(as_hex, expected):
        with patch('string_utils.generation.uuid4', return_value='mocked_uuid'):
            result = uuid(as_hex)
>           assert result == expected
E           AssertionError: assert 'mocked_uuid' == '97e3a716-6b3...-8128cb24d76b'
E             
E             - 97e3a716-6b33-4ab9-9bb1-8128cb24d76b
E             + mocked_uuid

python-string-utils/Test4DT_tests/test_string_utils_generation_uuid_0_test_valid_input_hex_format.py:14: AssertionError
______ test_valid_input_hex_format[True-97e3a7166b334ab99bb18128cb24d76b] ______

as_hex = True, expected = '97e3a7166b334ab99bb18128cb24d76b'

    @pytest.mark.parametrize("as_hex, expected", [
        (False, '97e3a716-6b33-4ab9-9bb1-8128cb24d76b'),
        (True, '97e3a7166b334ab99bb18128cb24d76b')
    ])
    def test_valid_input_hex_format(as_hex, expected):
        with patch('string_utils.generation.uuid4', return_value='mocked_uuid'):
>           result = uuid(as_hex)

python-string-utils/Test4DT_tests/test_string_utils_generation_uuid_0_test_valid_input_hex_format.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

as_hex = True

    def uuid(as_hex: bool = False) -> str:
        """
        Generated an UUID string (using `uuid.uuid4()`).
    
        *Examples:*
    
        >>> uuid() # possible output: '97e3a716-6b33-4ab9-9bb1-8128cb24d76b'
        >>> uuid(as_hex=True) # possible output: '97e3a7166b334ab99bb18128cb24d76b'
    
        :param as_hex: True to return the hex value of the UUID, False to get its default representation (default).
        :return: uuid string.
        """
        uid = uuid4()
    
        if as_hex:
>           return uid.hex
E           AttributeError: 'str' object has no attribute 'hex'

python-string-utils/string_utils/generation.py:36: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_generation_uuid_0_test_valid_input_hex_format.py::test_valid_input_hex_format[False-97e3a716-6b33-4ab9-9bb1-8128cb24d76b]
FAILED python-string-utils/Test4DT_tests/test_string_utils_generation_uuid_0_test_valid_input_hex_format.py::test_valid_input_hex_format[True-97e3a7166b334ab99bb18128cb24d76b]
============================== 2 failed in 0.03s ===============================
"""