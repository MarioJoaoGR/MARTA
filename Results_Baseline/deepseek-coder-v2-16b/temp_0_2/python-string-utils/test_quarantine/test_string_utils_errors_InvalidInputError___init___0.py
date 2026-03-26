
# Module: string_utils.errors
# test_string_utils.py
from string_utils.errors import InvalidInputError
import pytest
import zlib
import base64

def test_compress_valid_input():
    input_string = "Hello, World!"
    encoding = 'utf-8'
    compression_level = 9
    compressed_output = zlib.compress(input_string.encode(encoding), compression_level)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

python-string-utils/Test4DT_tests/test_string_utils_errors_InvalidInputError___init___0.py . [ 25%]
FF.                                                                      [100%]

=================================== FAILURES ===================================
___________________ test_compress_invalid_compression_level ____________________

    def test_compress_invalid_compression_level():
        input_string = "Hello, World!"
        encoding = 'utf-8'
        with pytest.raises(ValueError):
>           zlib.compress(input_string.encode(encoding), 10)  # Invalid compression level
E           zlib.error: Bad compression level

python-string-utils/Test4DT_tests/test_string_utils_errors_InvalidInputError___init___0.py:20: error
________________________ test_compress_invalid_encoding ________________________

    def test_compress_invalid_encoding():
        input_string = "Hello, World!"
        encoding = None  # Invalid encoding
        with pytest.raises(ValueError):
>           zlib.compress(input_string.encode(encoding))
E           TypeError: encode() argument 'encoding' must be str, not None

python-string-utils/Test4DT_tests/test_string_utils_errors_InvalidInputError___init___0.py:26: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_errors_InvalidInputError___init___0.py::test_compress_invalid_compression_level
FAILED python-string-utils/Test4DT_tests/test_string_utils_errors_InvalidInputError___init___0.py::test_compress_invalid_encoding
========================= 2 failed, 2 passed in 0.02s ==========================

"""