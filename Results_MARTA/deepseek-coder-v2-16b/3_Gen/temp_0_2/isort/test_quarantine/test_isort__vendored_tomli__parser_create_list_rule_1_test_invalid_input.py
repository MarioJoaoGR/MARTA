
from isort._vendored.tomli._parser import create_list_rule, Output, Pos, Key, Flags
import pytest

@pytest.fixture
def setup():
    src = "[[list]]\nkey=value"
    pos = 0
    out = Output(data=[], flags={})  # Provide initial data and flags
    return src, pos, out

def test_invalid_input(setup):
    src, pos, out = setup
    with pytest.raises(Exception) as e:
        create_list_rule(src, pos, out)
    assert str(e.value) == "Expected \"]]\" at the end of an array declaration"

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_create_list_rule_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

setup = ('[[list]]\nkey=value', 0, Output(data=[], flags={}))

    def test_invalid_input(setup):
        src, pos, out = setup
        with pytest.raises(Exception) as e:
            create_list_rule(src, pos, out)
>       assert str(e.value) == "Expected \"]]\" at the end of an array declaration"
E       assert "'dict' objec...tribute 'is_'" == 'Expected "]]...y declaration'
E         
E         - Expected "]]" at the end of an array declaration
E         + 'dict' object has no attribute 'is_'

isort/Test4DT_tests/test_isort__vendored_tomli__parser_create_list_rule_1_test_invalid_input.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_create_list_rule_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.12s ===============================
"""