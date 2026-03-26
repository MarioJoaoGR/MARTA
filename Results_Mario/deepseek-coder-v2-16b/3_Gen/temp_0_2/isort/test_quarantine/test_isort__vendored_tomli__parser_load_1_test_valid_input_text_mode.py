
import pytest
from io import StringIO, BytesIO
from isort._vendored.tomli._parser import loads
from typing import Dict, Any, IO

def load(fp: IO, *, parse_float: ParseFloat = float) -> Dict[str, Any]:
    """Parse TOML from a file object."""
    s = fp.read()
    if isinstance(s, bytes):
        s = s.decode()
    else:
        warnings.warn(
            "Text file object support is deprecated in favor of binary file objects."
            ' Use `open("foo.toml", "rb")` to open the file in binary mode.',
            DeprecationWarning,
        )
    return loads(s, parse_float=parse_float)

@pytest.fixture
def valid_toml():
    return """name = "Tom"
age = 42"""

def test_valid_input_text_mode(valid_toml):
    fp = StringIO(valid_toml)
    data = load(fp)
    assert isinstance(data, dict)
    assert data['name'] == "Tom"
    assert data['age'] == 42

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_load_1_test_valid_input_text_mode
isort/Test4DT_tests/test_isort__vendored_tomli__parser_load_1_test_valid_input_text_mode.py:7:33: E0602: Undefined variable 'ParseFloat' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_load_1_test_valid_input_text_mode.py:13:8: E0602: Undefined variable 'warnings' (undefined-variable)


"""