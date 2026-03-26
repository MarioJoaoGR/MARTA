
import pytest
from string_utils.manipulation import decompress

def test_valid_input():
    valid_base64 = "H4sIAAAAAAAAA0vMycnP18svL9JNzS/Rzywp1U3NLy7QVcgsKdZVzCwqAAAA"
    expected_output = "This is a test string."
    
    # Call the decompress function with valid input
    result = decompress(valid_base64, 'utf-8')
    
    assert result == expected_output

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation_decompress_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        valid_base64 = "H4sIAAAAAAAAA0vMycnP18svL9JNzS/Rzywp1U3NLy7QVcgsKdZVzCwqAAAA"
        expected_output = "This is a test string."
    
        # Call the decompress function with valid input
>       result = decompress(valid_base64, 'utf-8')

python-string-utils/Test4DT_tests/test_string_utils_manipulation_decompress_0_test_valid_input.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
python-string-utils/string_utils/manipulation.py:608: in decompress
    return __StringCompressor.decompress(input_string, encoding)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'string_utils.manipulation.__StringCompressor'>
input_string = 'H4sIAAAAAAAAA0vMycnP18svL9JNzS/Rzywp1U3NLy7QVcgsKdZVzCwqAAAA'
encoding = 'utf-8'

    @classmethod
    def decompress(cls, input_string: str, encoding: str = 'utf-8') -> str:
        cls.__require_valid_input_and_encoding(input_string, encoding)
    
        # turns input string into a sequence of bytes
        # (the string is assumed to be a previously compressed string, therefore we have to decode it using base64)
        input_bytes = base64.urlsafe_b64decode(input_string)
    
        # decompress bytes using zlib
>       decompressed_bytes = zlib.decompress(input_bytes)
E       zlib.error: Error -3 while decompressing data: incorrect header check

python-string-utils/string_utils/manipulation.py:204: error
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation_decompress_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.03s ===============================
"""