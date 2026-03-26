
import pytest
from isort._vendored.tomli._parser import parse_value, Pos

@pytest.mark.parametrize("src", ["42"])
def test_valid_number(src):
    pos = 0
    parsed_value, new_pos = parse_value(src, Pos(pos), float)
    assert isinstance(parsed_value, int)
    assert new_pos == len(src)

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_value_2_test_valid_number.py F [100%]

=================================== FAILURES ===================================
____________________________ test_valid_number[42] _____________________________

src = '42'

    @pytest.mark.parametrize("src", ["42"])
    def test_valid_number(src):
        pos = 0
        parsed_value, new_pos = parse_value(src, Pos(pos), float)
        assert isinstance(parsed_value, int)
>       assert new_pos == len(src)
E       AssertionError: assert 42 == 2
E        +  where 2 = len('42')

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_value_2_test_valid_number.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_value_2_test_valid_number.py::test_valid_number[42]
============================== 1 failed in 0.13s ===============================
"""