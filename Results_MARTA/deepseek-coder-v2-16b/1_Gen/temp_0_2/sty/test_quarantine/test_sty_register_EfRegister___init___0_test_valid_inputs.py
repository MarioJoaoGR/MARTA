
import pytest
from sty import EfRegister, Style, Sgr

@pytest.fixture
def ef():
    return EfRegister()

def test_valid_inputs(ef):
    # Test bold effect
    assert str(ef.bold) == "\033[1m"
    assert f"{ef.bold}Bold Text{ef.rs}" == "\033[1mBold Text\033[22m"

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

sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

ef = <sty.register.EfRegister object at 0x101d9ca00>

    def test_valid_inputs(ef):
        # Test bold effect
        assert str(ef.bold) == "\033[1m"
>       assert f"{ef.bold}Bold Text{ef.rs}" == "\033[1mBold Text\033[22m"
E       AssertionError: assert '\x1b[1mBold ...b[28m\x1b[29m' == '\x1b[1mBold Text\x1b[22m'
E         
E         - [1mBold Text[22m
E         + [1mBold Text[22m[23m[24m[25m[27m[28m[29m

sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_valid_inputs.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_register_EfRegister___init___0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.02s ===============================
"""