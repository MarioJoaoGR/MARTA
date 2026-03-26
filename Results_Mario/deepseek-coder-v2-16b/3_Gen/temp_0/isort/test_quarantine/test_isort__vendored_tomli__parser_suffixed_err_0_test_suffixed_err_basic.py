
from isort._vendored.tomli.parser import TOMLDecodeError  # Importing correctly from module 'isort._vendored.tomli._parser'

def suffixed_err(src: str, pos: int, msg: str) -> TOMLDecodeError:
    """Return a `TOMLDecodeError` where error message is suffixed with coordinates in source."""

    def coord_repr(src: str, pos: int) -> str:
        if pos >= len(src):
            return "end of document"
        line = src.count("\n", 0, pos) + 1
        column = pos - (src.rindex("\n", 0, pos) if line > 1 else pos) + 1
        return f"line {line}, column {column}"

    return TOMLDecodeError(f"{msg} (at {coord_repr(src, pos)})")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_suffixed_err_0_test_suffixed_err_basic
isort/Test4DT_tests/test_isort__vendored_tomli__parser_suffixed_err_0_test_suffixed_err_basic.py:2:0: E0401: Unable to import 'isort._vendored.tomli.parser' (import-error)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_suffixed_err_0_test_suffixed_err_basic.py:2:0: E0611: No name 'parser' in module 'isort._vendored.tomli' (no-name-in-module)


"""