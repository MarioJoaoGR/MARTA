
import pytest
from string_utils.manipulation import __StringCompressor

class TestStringCompressor:
    
    def test_valid_compression(self):
        input_string = "example text"
        encoding = 'utf-8'
        compression_level = 9
        compressed_text = __StringCompressor.compress(input_string, encoding, compression_level)
        assert isinstance(compressed_text, str), f"Expected a string but got {type(compressed_text).__name__}"
    
    def test_invalid_compression_level(self):
        input_string = "example text"
        encoding = 'utf-8'
        compression_level = 10
        with pytest.raises(ValueError):
            __StringCompressor.compress(input_string, encoding, compression_level)
    
    def test_empty_string(self):
        input_string = ""
        encoding = 'utf-8'
        with pytest.raises(ValueError):
            __StringCompressor.compress(input_string, encoding)
    
    def test_invalid_encoding(self):
        input_string = "example text"
        encoding = None
        with pytest.raises(ValueError):
            __StringCompressor.compress(input_string, encoding)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringCompressor_compress_0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
_________________ TestStringCompressor.test_valid_compression __________________

self = <test_string_utils_manipulation___StringCompressor_compress_0.TestStringCompressor object at 0x7f78e0909990>

    def test_valid_compression(self):
        input_string = "example text"
        encoding = 'utf-8'
        compression_level = 9
>       compressed_text = __StringCompressor.compress(input_string, encoding, compression_level)
E       NameError: name '_TestStringCompressor__StringCompressor' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringCompressor_compress_0.py:11: NameError
_____________ TestStringCompressor.test_invalid_compression_level ______________

self = <test_string_utils_manipulation___StringCompressor_compress_0.TestStringCompressor object at 0x7f78e090b1c0>

    def test_invalid_compression_level(self):
        input_string = "example text"
        encoding = 'utf-8'
        compression_level = 10
        with pytest.raises(ValueError):
>           __StringCompressor.compress(input_string, encoding, compression_level)
E           NameError: name '_TestStringCompressor__StringCompressor' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringCompressor_compress_0.py:19: NameError
____________________ TestStringCompressor.test_empty_string ____________________

self = <test_string_utils_manipulation___StringCompressor_compress_0.TestStringCompressor object at 0x7f78e090b040>

    def test_empty_string(self):
        input_string = ""
        encoding = 'utf-8'
        with pytest.raises(ValueError):
>           __StringCompressor.compress(input_string, encoding)
E           NameError: name '_TestStringCompressor__StringCompressor' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringCompressor_compress_0.py:25: NameError
__________________ TestStringCompressor.test_invalid_encoding __________________

self = <test_string_utils_manipulation___StringCompressor_compress_0.TestStringCompressor object at 0x7f78e090ac80>

    def test_invalid_encoding(self):
        input_string = "example text"
        encoding = None
        with pytest.raises(ValueError):
>           __StringCompressor.compress(input_string, encoding)
E           NameError: name '_TestStringCompressor__StringCompressor' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringCompressor_compress_0.py:31: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringCompressor_compress_0.py::TestStringCompressor::test_valid_compression
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringCompressor_compress_0.py::TestStringCompressor::test_invalid_compression_level
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringCompressor_compress_0.py::TestStringCompressor::test_empty_string
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation___StringCompressor_compress_0.py::TestStringCompressor::test_invalid_encoding
============================== 4 failed in 0.07s ===============================
"""