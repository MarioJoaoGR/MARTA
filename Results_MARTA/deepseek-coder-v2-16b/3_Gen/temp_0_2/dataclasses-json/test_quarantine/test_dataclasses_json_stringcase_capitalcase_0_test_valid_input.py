
import pytest
from dataclasses_json.stringcase import capitalcase

@pytest.mark.parametrize("input_string, expected", [
    ("hello", "Hello"),
    ("HELLO WORLD", "Hello world"),
    ("", ""),
    (12345, str(12345))  # Convert integer to string for comparison
])
def test_valid_input(input_string, expected):
    assert capitalcase(input_string) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_capitalcase_0_test_valid_input.py . [ 25%]
F..                                                                      [100%]

=================================== FAILURES ===================================
__________________ test_valid_input[HELLO WORLD-Hello world] ___________________

input_string = 'HELLO WORLD', expected = 'Hello world'

    @pytest.mark.parametrize("input_string, expected", [
        ("hello", "Hello"),
        ("HELLO WORLD", "Hello world"),
        ("", ""),
        (12345, str(12345))  # Convert integer to string for comparison
    ])
    def test_valid_input(input_string, expected):
>       assert capitalcase(input_string) == expected
E       AssertionError: assert 'HELLO WORLD' == 'Hello world'
E         
E         - Hello world
E         + HELLO WORLD

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_capitalcase_0_test_valid_input.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_capitalcase_0_test_valid_input.py::test_valid_input[HELLO WORLD-Hello world]
========================= 1 failed, 3 passed in 0.03s ==========================
"""