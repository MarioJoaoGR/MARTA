
import pytest
from io import BytesIO
from toml import load as toml_load, TOMLDecodeError

def test_invalid_file():
    with open('example.toml', 'wb') as fp:
        fp.write(b'Invalid TOML')
    
    with pytest.raises(TOMLDecodeError):
        with open('example.toml', 'rb') as fp:
            toml_load(fp)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_load_0_test_invalid_file
isort/Test4DT_tests/test_isort__vendored_tomli__parser_load_0_test_invalid_file.py:4:0: E0611: No name 'TOMLDecodeError' in module 'toml' (no-name-in-module)


"""