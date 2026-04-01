
import pytest
from string_utils.manipulation import decompress

def test_empty_string():
    with pytest.raises(ValueError, match="Input string cannot be empty."):
        decompress("")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation_decompress_0_test_empty_string.py F [100%]

=================================== FAILURES ===================================
______________________________ test_empty_string _______________________________

    def test_empty_string():
        with pytest.raises(ValueError, match="Input string cannot be empty."):
>           decompress("")

python-string-utils/Test4DT_tests/test_string_utils_manipulation_decompress_0_test_empty_string.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
python-string-utils/string_utils/manipulation.py:608: in decompress
    return __StringCompressor.decompress(input_string, encoding)
python-string-utils/string_utils/manipulation.py:197: in decompress
    cls.__require_valid_input_and_encoding(input_string, encoding)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_string = '', encoding = 'utf-8'

    @staticmethod
    def __require_valid_input_and_encoding(input_string: str, encoding: str):
        if not is_string(input_string):
            raise InvalidInputError(input_string)
    
        if len(input_string) == 0:
>           raise ValueError('Input string cannot be empty')
E           ValueError: Input string cannot be empty

python-string-utils/string_utils/manipulation.py:167: ValueError

During handling of the above exception, another exception occurred:

    def test_empty_string():
>       with pytest.raises(ValueError, match="Input string cannot be empty."):
E       AssertionError: Regex pattern did not match.
E        Regex: 'Input string cannot be empty.'
E        Input: 'Input string cannot be empty'

python-string-utils/Test4DT_tests/test_string_utils_manipulation_decompress_0_test_empty_string.py:6: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation_decompress_0_test_empty_string.py::test_empty_string
============================== 1 failed in 0.03s ===============================
"""