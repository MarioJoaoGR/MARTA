
import pytest
from isort._vendored.tomli._parser import loads
from io import StringIO
from typing import Dict, Any, IO
import warnings

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

def test_invalid_file_mode():
    with pytest.raises(TypeError):
        with open("sample.toml", "w") as fp:
            load(fp)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_load_2_test_invalid_file_mode
isort/Test4DT_tests/test_isort__vendored_tomli__parser_load_2_test_invalid_file_mode.py:8:33: E0602: Undefined variable 'ParseFloat' (undefined-variable)


"""