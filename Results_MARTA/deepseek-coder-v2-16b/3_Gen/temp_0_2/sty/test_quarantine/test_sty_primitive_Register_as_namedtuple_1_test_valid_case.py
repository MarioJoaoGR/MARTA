
from sty import primitive
from unittest.mock import MagicMock
from collections import namedtuple
import pytest

@pytest.fixture(autouse=True)
def mock_register():
    register = primitive.Register()
    register.as_dict = MagicMock(return_value={"renderfuncs": {}, "is_muted": False, "eightbit_call": lambda x: x, "rgb_call": lambda r, g, b: (r, g, b)})
    return register

def test_valid_case(mock_register):
    result = mock_register.as_namedtuple()
    
    ExpectedStyleRegister = namedtuple("StyleRegister", ["renderfuncs", "is_muted", "eightbit_call", "rgb_call"])
    expected_values = {"renderfuncs": {}, "is_muted": False, "eightbit_call": lambda x: x, "rgb_call": lambda r, g, b: (r, g, b)}
    
    assert isinstance(result, ExpectedStyleRegister)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/sty
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

sty/Test4DT_tests/test_sty_primitive_Register_as_namedtuple_1_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

mock_register = <sty.primitive.Register object at 0x105b4cd00>

    def test_valid_case(mock_register):
        result = mock_register.as_namedtuple()
    
        ExpectedStyleRegister = namedtuple("StyleRegister", ["renderfuncs", "is_muted", "eightbit_call", "rgb_call"])
        expected_values = {"renderfuncs": {}, "is_muted": False, "eightbit_call": lambda x: x, "rgb_call": lambda r, g, b: (r, g, b)}
    
>       assert isinstance(result, ExpectedStyleRegister)
E       AssertionError: assert False
E        +  where False = isinstance(StyleRegister(renderfuncs={}, is_muted=False, eightbit_call=<function mock_register.<locals>.<lambda> at 0x105b59630>, rgb_call=<function mock_register.<locals>.<lambda> at 0x105b596c0>), <class 'Test4DT_tests.test_sty_primitive_Register_as_namedtuple_1_test_valid_case.StyleRegister'>)

sty/Test4DT_tests/test_sty_primitive_Register_as_namedtuple_1_test_valid_case.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register_as_namedtuple_1_test_valid_case.py::test_valid_case
============================== 1 failed in 0.02s ===============================
"""