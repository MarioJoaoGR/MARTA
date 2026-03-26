
# Module: isort.wrap_modes
# test_vertical_hanging_indent_bracket.py
from isort.wrap_modes import vertical_hanging_indent_bracket
import pytest
from typing import Any

def test_basic_usage():
    interface = {
        "imports": ["os", "sys"],
        "indent": "    "
    }
    result = vertical_hanging_indent_bracket(**interface)
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

isort/Test4DT_tests/test_isort_wrap_modes_vertical_hanging_indent_bracket_0.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_basic_usage _______________________________

    def test_basic_usage():
        interface = {
            "imports": ["os", "sys"],
            "indent": "    "
        }
>       result = vertical_hanging_indent_bracket(**interface)

isort/Test4DT_tests/test_isort_wrap_modes_vertical_hanging_indent_bracket_0.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/wrap_modes.py:267: in vertical_hanging_indent_bracket
    statement = vertical_hanging_indent(**interface)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

interface = {'imports': ['os', 'sys'], 'indent': '    '}

    @_wrap_mode
    def vertical_hanging_indent(**interface: Any) -> str:
        _line_with_comments = isort.comments.add_to_line(
>           interface["comments"],
            "",
            removed=interface["remove_comments"],
            comment_prefix=interface["comment_prefix"],
        )
E       KeyError: 'comments'

isort/isort/wrap_modes.py:173: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_wrap_modes_vertical_hanging_indent_bracket_0.py::test_basic_usage
============================== 1 failed in 0.10s ===============================
"""