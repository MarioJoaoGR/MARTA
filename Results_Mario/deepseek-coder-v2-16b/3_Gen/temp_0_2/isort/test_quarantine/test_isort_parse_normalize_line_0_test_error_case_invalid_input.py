
import pytest
from isort import parse

@pytest.mark.parametrize("raw_line", [
    "",  # Empty string
    None,  # None type
    [],  # List (invalid input)
    123,  # Integer (invalid input)
])
def test_error_case_invalid_input(raw_line):
    with pytest.raises(TypeError):
        parse.normalize_line(raw_line)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

isort/Test4DT_tests/test_isort_parse_normalize_line_0_test_error_case_invalid_input.py F [ 25%]
...                                                                      [100%]

=================================== FAILURES ===================================
_______________________ test_error_case_invalid_input[] ________________________

raw_line = ''

    @pytest.mark.parametrize("raw_line", [
        "",  # Empty string
        None,  # None type
        [],  # List (invalid input)
        123,  # Integer (invalid input)
    ])
    def test_error_case_invalid_input(raw_line):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

isort/Test4DT_tests/test_isort_parse_normalize_line_0_test_error_case_invalid_input.py:12: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_parse_normalize_line_0_test_error_case_invalid_input.py::test_error_case_invalid_input[]
========================= 1 failed, 3 passed in 0.11s ==========================
"""