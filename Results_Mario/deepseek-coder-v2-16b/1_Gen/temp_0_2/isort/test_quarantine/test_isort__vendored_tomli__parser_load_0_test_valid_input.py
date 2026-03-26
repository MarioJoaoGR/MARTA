
from isort._vendored.tomli._parser import loads
from typing import Dict, Any, IO, List
import pytest

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

# Test case for valid input
def test_valid_input():
    toml_content = """key = "value"
array = [1, 2, 3]"""
    fp = io.StringIO(toml_content)
    parsed_data = load(fp)
    assert isinstance(parsed_data, dict)
    assert parsed_data['key'] == 'value'
    assert parsed_data['array'] == [1, 2, 3]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_load_0_test_valid_input
isort/Test4DT_tests/test_isort__vendored_tomli__parser_load_0_test_valid_input.py:6:33: E0602: Undefined variable 'ParseFloat' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_load_0_test_valid_input.py:12:8: E0602: Undefined variable 'warnings' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_load_0_test_valid_input.py:23:9: E0602: Undefined variable 'io' (undefined-variable)


"""