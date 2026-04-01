
import pytest
from sty import primitive

@pytest.fixture(scope="module")
def custom_register():
    return primitive.Register()

def test_valid_inputs(custom_register):
    # Test standard inputs for fg(42), bg(102, 49, 42), and muted state
    
    # Set foreground color (8-bit)
    assert custom_register(42) == "42"
    
    # Set background color (24-bit)
    assert custom_register(102, 49, 42) == "(102, 49, 42)"
    
    # Muting the register temporarily
    custom_register.is_muted = True
    assert custom_register() == ""

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

sty/Test4DT_tests/test_sty_primitive_Register___call___0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

custom_register = <sty.primitive.Register object at 0x101f04520>

    def test_valid_inputs(custom_register):
        # Test standard inputs for fg(42), bg(102, 49, 42), and muted state
    
        # Set foreground color (8-bit)
>       assert custom_register(42) == "42"
E       AssertionError: assert 42 == '42'
E        +  where 42 = <sty.primitive.Register object at 0x101f04520>(42)

sty/Test4DT_tests/test_sty_primitive_Register___call___0_test_valid_inputs.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register___call___0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.02s ===============================
"""