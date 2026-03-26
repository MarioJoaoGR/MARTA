
import pytest
from unittest.mock import patch
from string_utils.manipulation import reverse, is_string, InvalidInputError

@pytest.mark.parametrize("input_string, expected", [
    (None, None),  # Edge case: input is None
])
def test_edge_case_none(input_string, expected):
    with patch('string_utils.manipulation.is_string', return_value=True):
        if input_string is not None:
            assert reverse(input_string) == expected
        else:
            with pytest.raises(InvalidInputError):
                reverse(input_string)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation_reverse_1_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
________________________ test_edge_case_none[None-None] ________________________

input_string = None, expected = None

    @pytest.mark.parametrize("input_string, expected", [
        (None, None),  # Edge case: input is None
    ])
    def test_edge_case_none(input_string, expected):
        with patch('string_utils.manipulation.is_string', return_value=True):
            if input_string is not None:
                assert reverse(input_string) == expected
            else:
                with pytest.raises(InvalidInputError):
>                   reverse(input_string)

python-string-utils/Test4DT_tests/test_string_utils_manipulation_reverse_1_test_edge_case_none.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_string = None

    def reverse(input_string: str) -> str:
        """
        Returns the string with its chars reversed.
    
        *Example:*
    
        >>> reverse('hello') # returns 'olleh'
    
        :param input_string: String to revert.
        :type input_string: str
        :return: Reversed string.
        """
        if not is_string(input_string):
            raise InvalidInputError(input_string)
    
>       return input_string[::-1]
E       TypeError: 'NoneType' object is not subscriptable

python-string-utils/string_utils/manipulation.py:297: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation_reverse_1_test_edge_case_none.py::test_edge_case_none[None-None]
============================== 1 failed in 0.04s ===============================

"""