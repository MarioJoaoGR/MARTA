
import pytest
from isort.format import remove_whitespace

@pytest.mark.parametrize("input_str, expected", [
    ("Hello, World!", "Hello,World!"),
    ("This is a test.", "Thisisatest."),
    ("Remove \n all \t newlines and spaces", "Removeallnewlinesandspaces"),
])
def test_valid_input(input_str, expected):
    assert remove_whitespace(input_str) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

isort/Test4DT_tests/test_isort_format_remove_whitespace_3_test_valid_input.py . [ 33%]
.F                                                                       [100%]

=================================== FAILURES ===================================
_ test_valid_input[Remove \n all \t newlines and spaces-Removeallnewlinesandspaces] _

input_str = 'Remove \n all \t newlines and spaces'
expected = 'Removeallnewlinesandspaces'

    @pytest.mark.parametrize("input_str, expected", [
        ("Hello, World!", "Hello,World!"),
        ("This is a test.", "Thisisatest."),
        ("Remove \n all \t newlines and spaces", "Removeallnewlinesandspaces"),
    ])
    def test_valid_input(input_str, expected):
>       assert remove_whitespace(input_str) == expected
E       AssertionError: assert 'Removeall\tnewlinesandspaces' == 'Removeallnewlinesandspaces'
E         
E         - Removeallnewlinesandspaces
E         + Removeall	newlinesandspaces
E         ?          +

isort/Test4DT_tests/test_isort_format_remove_whitespace_3_test_valid_input.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_format_remove_whitespace_3_test_valid_input.py::test_valid_input[Remove \n all \t newlines and spaces-Removeallnewlinesandspaces]
========================= 1 failed, 2 passed in 0.13s ==========================
"""