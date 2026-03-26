
import pytest
from string_utils.manipulation import __StringCompressor
import base64
import zlib

@pytest.mark.parametrize("input_string, encoding", [
    ("example", "utf-8"),  # This should pass as the input is valid
    ("", None),            # This should raise ValueError for empty input
    (None, "utf-8")        # This should raise TypeError for missing input
])
def test_invalid_encoding(input_string, encoding):
    with pytest.raises(ValueError) if isinstance(input_string, str) and input_string == "" else pytest.raises(TypeError):
        __StringCompressor.decompress(input_string, encoding)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor_decompress_0_test_invalid_encoding.py F [ 33%]
..                                                                       [100%]

=================================== FAILURES ===================================
_____________________ test_invalid_encoding[example-utf-8] _____________________

input_string = 'example', encoding = 'utf-8'

    @pytest.mark.parametrize("input_string, encoding", [
        ("example", "utf-8"),  # This should pass as the input is valid
        ("", None),            # This should raise ValueError for empty input
        (None, "utf-8")        # This should raise TypeError for missing input
    ])
    def test_invalid_encoding(input_string, encoding):
        with pytest.raises(ValueError) if isinstance(input_string, str) and input_string == "" else pytest.raises(TypeError):
>           __StringCompressor.decompress(input_string, encoding)

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor_decompress_0_test_invalid_encoding.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
python-string-utils/string_utils/manipulation.py:201: in decompress
    input_bytes = base64.urlsafe_b64decode(input_string)
/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/base64.py:133: in urlsafe_b64decode
    return b64decode(s)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

s = b'example', altchars = None, validate = False

    def b64decode(s, altchars=None, validate=False):
        """Decode the Base64 encoded bytes-like object or ASCII string s.
    
        Optional altchars must be a bytes-like object or ASCII string of length 2
        which specifies the alternative alphabet used instead of the '+' and '/'
        characters.
    
        The result is returned as a bytes object.  A binascii.Error is raised if
        s is incorrectly padded.
    
        If validate is False (the default), characters that are neither in the
        normal base-64 alphabet nor the alternative alphabet are discarded prior
        to the padding check.  If validate is True, these non-alphabet characters
        in the input result in a binascii.Error.
        """
        s = _bytes_from_decode_data(s)
        if altchars is not None:
            altchars = _bytes_from_decode_data(altchars)
            assert len(altchars) == 2, repr(altchars)
            s = s.translate(bytes.maketrans(altchars, b'+/'))
        if validate and not re.fullmatch(b'[A-Za-z0-9+/]*={0,2}', s):
            raise binascii.Error('Non-base64 digit found')
>       return binascii.a2b_base64(s)
E       binascii.Error: Incorrect padding

/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/base64.py:87: Error
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor_decompress_0_test_invalid_encoding.py::test_invalid_encoding[example-utf-8]
========================= 1 failed, 2 passed in 0.05s ==========================

"""