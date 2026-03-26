
from isort._vendored.tomli.parser import parser
import pytest
from tomllib import TOMLDecodeError

def suffixed_err(src: str, pos: int, msg: str) -> TOMLDecodeError:
    """Return a `TOMLDecodeError` where error message is suffixed with coordinates in source."""

    def coord_repr(src: str, pos: int) -> str:
        if pos >= len(src):
            return "end of document"
        line = src.count("\n", 0, pos) + 1
        column = pos - src.rindex("\n", 0, pos) if line > 1 else pos + 1
        return f"line {line}, column {column}"

    return TOMLDecodeError(f"{msg} (at {coord_repr(src, pos)})")

# Example usage:
if __name__ == "__main__":
    src = "def example():\n    return x\n"
    pos = 10
    msg = "Unexpected token 'x'"
    err = suffixed_err(src, pos, msg)
    print(err)  # Outputs: Unexpected token 'x' (at line 2, column 4)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_suffixed_err_0_test_edge_case_none
isort/Test4DT_tests/test_isort__vendored_tomli__parser_suffixed_err_0_test_edge_case_none.py:2:0: E0401: Unable to import 'isort._vendored.tomli.parser' (import-error)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_suffixed_err_0_test_edge_case_none.py:2:0: E0611: No name 'parser' in module 'isort._vendored.tomli' (no-name-in-module)


"""