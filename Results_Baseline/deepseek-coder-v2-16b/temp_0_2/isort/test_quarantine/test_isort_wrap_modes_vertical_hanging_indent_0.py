
# Module: isort.wrap_modes
# test_vertical_hanging_indent.py
from isort.wrap_modes import vertical_hanging_indent

def test_vertical_hanging_indent_basic():
    result = vertical_hanging_indent(
        comments=["This is a comment."],
        remove_comments=False,
        comment_prefix="#",
        line_separator="\n",
        indent="    ",
        imports=["math", "os"],
        include_trailing_comma=True,
        statement="from .. import utils"
    )
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

isort/Test4DT_tests/test_isort_wrap_modes_vertical_hanging_indent_0.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
______________________ test_vertical_hanging_indent_basic ______________________

    def test_vertical_hanging_indent_basic():
        result = vertical_hanging_indent(
            comments=["This is a comment."],
            remove_comments=False,
            comment_prefix="#",
            line_separator="\n",
            indent="    ",
            imports=["math", "os"],
            include_trailing_comma=True,
            statement="from .. import utils"
        )
>       assert result == 'from .. import utils( # This is a comment.\n    math, os)', "The function should include the comment in the output."
E       AssertionError: The function should include the comment in the output.
E       assert 'from .. impo...,\n    os,\n)' == 'from .. impo...    math, os)'
E         
E         - from .. import utils( # This is a comment.
E         ?                      -
E         + from .. import utils(# This is a comment.
E         -     math, os)
E         ?          ^^^^
E         +     math,...
E         
E         ...Full output truncated (3 lines hidden), use '-vv' to show

isort/Test4DT_tests/test_isort_wrap_modes_vertical_hanging_indent_0.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_wrap_modes_vertical_hanging_indent_0.py::test_vertical_hanging_indent_basic
========================= 1 failed, 1 passed in 0.10s ==========================
"""