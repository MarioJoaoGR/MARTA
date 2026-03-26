
import pytest
from isort._vendored.tomli._parser import TOMLDecodeError

def suffixed_err(src: str, pos: int, msg: str) -> TOMLDecodeError:
    """Return a `TOMLDecodeError` where error message is suffixed with coordinates in source."""

    def coord_repr(src: str, pos: int) -> str:
        if pos >= len(src):
            return "end of document"
        line = src.count("\n", 0, pos) + 1
        column = pos - (src.rindex("\n", 0, pos) if line > 1 else pos) + 1
        return f"line {line}, column {column}"

    return TOMLDecodeError(f"{msg} (at {coord_repr(src, pos)})")

def test_invalid_input():
    src = "def example():\n    return x\n"
    pos = 10
    msg = "Unexpected token 'x'"
    
    with pytest.raises(TOMLDecodeError):
        suffixed_err(src, pos, msg)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort__vendored_tomli__parser_suffixed_err_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        src = "def example():\n    return x\n"
        pos = 10
        msg = "Unexpected token 'x'"
    
>       with pytest.raises(TOMLDecodeError):
E       Failed: DID NOT RAISE <class 'isort._vendored.tomli._parser.TOMLDecodeError'>

isort/Test4DT_tests/test_isort__vendored_tomli__parser_suffixed_err_0_test_invalid_input.py:22: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_suffixed_err_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.10s ===============================
"""