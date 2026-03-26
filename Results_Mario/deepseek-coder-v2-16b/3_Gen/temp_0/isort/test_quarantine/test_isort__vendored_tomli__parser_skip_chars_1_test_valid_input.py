
import pytest
from typing import Iterable

# Assuming Pos is defined somewhere in your codebase or module
class Pos:
    def __init__(self, value):
        self.value = value

def skip_chars(src: str, pos: Pos, chars: Iterable[str]) -> Pos:
    try:
        while src[pos.value] in chars:
            pos.value += 1
    except IndexError:
        pass
    return pos

# Test case for valid input
def test_skip_chars_valid_input():
    result = skip_chars("hello world", Pos(0), ["l", "o"])
    assert result.value == 5

# Run the test
if __name__ == "__main__":
    pytest.main()

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_1_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_________________________ test_skip_chars_valid_input __________________________

    def test_skip_chars_valid_input():
        result = skip_chars("hello world", Pos(0), ["l", "o"])
>       assert result.value == 5
E       assert 0 == 5
E        +  where 0 = <Test4DT_tests.test_isort__vendored_tomli__parser_skip_chars_1_test_valid_input.Pos object at 0x7fd8ab101910>.value

isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_1_test_valid_input.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_1_test_valid_input.py::test_skip_chars_valid_input
============================== 1 failed in 0.09s ===============================
"""