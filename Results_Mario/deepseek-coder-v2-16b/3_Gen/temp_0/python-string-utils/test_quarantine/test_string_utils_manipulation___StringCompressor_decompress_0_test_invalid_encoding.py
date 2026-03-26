
import pytest
import base64
import zlib
from string_utils.manipulation import __StringCompressor

def test_invalid_encoding():
    with pytest.raises(ValueError) as excinfo:
        __StringCompressor.decompress("")
    assert str(excinfo.value) == "Input string cannot be empty."

def test_valid_encoding():
    compressed = base64.urlsafe_b64encode("original_string".encode('utf-8')).decode('utf-8')
    decompressed = __StringCompressor.decompress(compressed, 'utf-8')
    assert decompressed == "original_string"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor_decompress_0_test_invalid_encoding.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_invalid_encoding _____________________________

    def test_invalid_encoding():
        with pytest.raises(ValueError) as excinfo:
            __StringCompressor.decompress("")
>       assert str(excinfo.value) == "Input string cannot be empty."
E       AssertionError: assert 'Input string cannot be empty' == 'Input string...not be empty.'
E         
E         - Input string cannot be empty.
E         ?                             -
E         + Input string cannot be empty

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor_decompress_0_test_invalid_encoding.py:10: AssertionError
_____________________________ test_valid_encoding ______________________________

    def test_valid_encoding():
        compressed = base64.urlsafe_b64encode("original_string".encode('utf-8')).decode('utf-8')
>       decompressed = __StringCompressor.decompress(compressed, 'utf-8')

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor_decompress_0_test_invalid_encoding.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'string_utils.manipulation.__StringCompressor'>
input_string = 'b3JpZ2luYWxfc3RyaW5n', encoding = 'utf-8'

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
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor_decompress_0_test_invalid_encoding.py::test_invalid_encoding
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor_decompress_0_test_invalid_encoding.py::test_valid_encoding
============================== 2 failed in 0.03s ===============================
"""