
import base64
import zlib
from string_utils.manipulation import __StringCompressor

class Test__StringCompressorDecompressEmptyString(unittest.TestCase):
    def test_empty_string(self):
        with self.assertRaises(ValueError) as context:
            decompressed = __StringCompressor.decompress("")
        self.assertTrue('Input string cannot be empty.' in str(context.exception))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringCompressor_decompress_0_test_empty_string
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor_decompress_0_test_empty_string.py:6:50: E0602: Undefined variable 'unittest' (undefined-variable)


"""