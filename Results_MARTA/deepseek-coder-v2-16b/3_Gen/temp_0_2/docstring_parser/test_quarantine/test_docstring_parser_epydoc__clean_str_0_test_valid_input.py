
import pytest
from typing import Optional as T

def _clean_str(string: str) -> T.Optional[str]:
    string = string.strip()
    if len(string) > 0:
        return string
    return None

@pytest.mark.parametrize("input_string, expected", [
    ("Hello, World!", "Hello, World!"),
    ("   Hello, World!   ", "Hello, World!"),
    ("", None),
    ("     ", None),
])
def test_valid_input(input_string, expected):
    assert _clean_str(input_string) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests/test_docstring_parser_epydoc__clean_str_0_test_valid_input.py _
docstring_parser/Test4DT_tests/test_docstring_parser_epydoc__clean_str_0_test_valid_input.py:5: in <module>
    def _clean_str(string: str) -> T.Optional[str]:
/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/typing.py:375: in __getattr__
    raise AttributeError(item)
E   AttributeError: Optional
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR docstring_parser/Test4DT_tests/test_docstring_parser_epydoc__clean_str_0_test_valid_input.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.06s ===============================
"""