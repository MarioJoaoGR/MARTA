
import pytest
from string_utils.manipulation import __StringCompressor
import zlib
import base64

def test_invalid_input():
    with pytest.raises(ValueError):
        __StringCompressor.compress("")
    
    with pytest.raises(ValueError):
        __StringCompressor.compress("example", compression_level=-1)
    
    with pytest.raises(ValueError):
        __StringCompressor.compress("example", compression_level=10)
    
    with pytest.raises(ValueError):
        __StringCompressor.compress("example", encoding="invalid_encoding")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor_compress_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(ValueError):
            __StringCompressor.compress("")
    
        with pytest.raises(ValueError):
            __StringCompressor.compress("example", compression_level=-1)
    
        with pytest.raises(ValueError):
            __StringCompressor.compress("example", compression_level=10)
    
        with pytest.raises(ValueError):
>           __StringCompressor.compress("example", encoding="invalid_encoding")

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor_compress_1_test_invalid_input.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'string_utils.manipulation.__StringCompressor'>
input_string = 'example', encoding = 'invalid_encoding', compression_level = 9

    @classmethod
    def compress(cls, input_string: str, encoding: str = 'utf-8', compression_level: int = 9) -> str:
        cls.__require_valid_input_and_encoding(input_string, encoding)
    
        if not isinstance(compression_level, int) or compression_level < 0 or compression_level > 9:
            raise ValueError('Invalid compression_level: it must be an "int" between 0 and 9')
    
        # turns input string into a sequence of bytes using provided encoding
>       original_bytes = input_string.encode(encoding)
E       LookupError: unknown encoding: invalid_encoding

python-string-utils/string_utils/manipulation.py:180: LookupError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor_compress_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.03s ===============================
"""