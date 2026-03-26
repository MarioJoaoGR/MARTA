
import pytest
from isort.format import remove_whitespace

@pytest.mark.parametrize("input_content, expected_output", [
    ("No changes here  ", "Nochangeshere"),
    ("This is a test.\nThis is only a test.", "Thisisatest.Thisisonlyateast."),
    ("Hello, World!", "Hello,World!")
])
def test_whitespace_removal(input_content, expected_output):
    assert remove_whitespace(input_content) == expected_output

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

isort/Test4DT_tests/test_isort_format_remove_whitespace_0_test_whitespace_removal.py . [ 33%]
F.                                                                       [100%]

=================================== FAILURES ===================================
_ test_whitespace_removal[This is a test.\nThis is only a test.-Thisisatest.Thisisonlyateast.] _

input_content = 'This is a test.\nThis is only a test.'
expected_output = 'Thisisatest.Thisisonlyateast.'

    @pytest.mark.parametrize("input_content, expected_output", [
        ("No changes here  ", "Nochangeshere"),
        ("This is a test.\nThis is only a test.", "Thisisatest.Thisisonlyateast."),
        ("Hello, World!", "Hello,World!")
    ])
    def test_whitespace_removal(input_content, expected_output):
>       assert remove_whitespace(input_content) == expected_output
E       AssertionError: assert 'Thisisatest.Thisisonlyatest.' == 'Thisisatest....isonlyateast.'
E         
E         - Thisisatest.Thisisonlyateast.
E         ?                          -
E         + Thisisatest.Thisisonlyatest.

isort/Test4DT_tests/test_isort_format_remove_whitespace_0_test_whitespace_removal.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_format_remove_whitespace_0_test_whitespace_removal.py::test_whitespace_removal[This is a test.\nThis is only a test.-Thisisatest.Thisisonlyateast.]
========================= 1 failed, 2 passed in 0.12s ==========================
"""