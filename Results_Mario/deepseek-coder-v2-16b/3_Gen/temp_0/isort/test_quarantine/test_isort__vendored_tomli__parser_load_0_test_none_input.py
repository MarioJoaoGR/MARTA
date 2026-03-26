
from isort._vendored.tomli._parser import loads
import io
import warnings

def load(fp: io.IOBase, *, parse_float: ParseFloat = float) -> dict:
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

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_load_0_test_none_input
isort/Test4DT_tests/test_isort__vendored_tomli__parser_load_0_test_none_input.py:6:40: E0602: Undefined variable 'ParseFloat' (undefined-variable)


"""