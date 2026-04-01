
import pytest
from io import StringIO
from isort._vendored.tomli._parser import loads
from typing import Dict, Any, IO, Callable

ParseFloat = Callable[[str], float]

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

def test_valid_input():
    valid_toml = """name = "Tom"
age = 42
numbers = [1, 2, 3]
[preferences]
color = "blue"""
    
    fp = StringIO(valid_toml)
    parsed_data = load(fp)
    
    assert isinstance(parsed_data, dict)
    assert parsed_data['name'] == 'Tom'
    assert parsed_data['age'] == 42
    assert parsed_data['numbers'] == [1, 2, 3]
    assert parsed_data['preferences']['color'] == 'blue'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_load_0_test_valid_input
isort/Test4DT_tests/test_isort__vendored_tomli__parser_load_0_test_valid_input.py:15:8: E0602: Undefined variable 'warnings' (undefined-variable)


"""