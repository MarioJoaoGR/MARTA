
import pytest
from isort.output import _ensure_newline_before_comment

@pytest.mark.parametrize("input_lines, expected", [
    (["def function():", "    print('Hello, World!')", "# This is a comment"], ["", "def function():", "    print('Hello, World!')", "# This is a comment"]),
    (["print('Hello, World!')", "# This is a comment", "if __name__ == '__main__':", "    pass"], ["print('Hello, World!')", "", "# This is a comment", "if __name__ == '__main__':", "    pass"])
])
def test_ensure_newline_before_comment(input_lines, expected):
    assert _ensure_newline_before_comment(input_lines) == expected

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

isort/Test4DT_tests/test_isort_output__ensure_newline_before_comment_0_test__ensure_newline_before_comment_basic.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
__________ test_ensure_newline_before_comment[input_lines0-expected0] __________

input_lines = ['def function():', "    print('Hello, World!')", '# This is a comment']
expected = ['', 'def function():', "    print('Hello, World!')", '# This is a comment']

    @pytest.mark.parametrize("input_lines, expected", [
        (["def function():", "    print('Hello, World!')", "# This is a comment"], ["", "def function():", "    print('Hello, World!')", "# This is a comment"]),
        (["print('Hello, World!')", "# This is a comment", "if __name__ == '__main__':", "    pass"], ["print('Hello, World!')", "", "# This is a comment", "if __name__ == '__main__':", "    pass"])
    ])
    def test_ensure_newline_before_comment(input_lines, expected):
>       assert _ensure_newline_before_comment(input_lines) == expected
E       AssertionError: assert ['def functio...is a comment'] == ['', 'def fun...is a comment']
E         
E         At index 0 diff: 'def function():' != ''
E         Use -v to get more diff

isort/Test4DT_tests/test_isort_output__ensure_newline_before_comment_0_test__ensure_newline_before_comment_basic.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_output__ensure_newline_before_comment_0_test__ensure_newline_before_comment_basic.py::test_ensure_newline_before_comment[input_lines0-expected0]
========================= 1 failed, 1 passed in 0.10s ==========================
"""