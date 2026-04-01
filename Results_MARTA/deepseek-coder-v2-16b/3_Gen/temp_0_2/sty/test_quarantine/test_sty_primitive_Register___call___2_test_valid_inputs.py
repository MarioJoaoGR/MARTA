
import pytest
from sty.primitive import Register

@pytest.fixture
def custom_register():
    return Register()

def test_valid_inputs(custom_register):
    # Test setting 8-bit color code
    assert custom_register(42) == "42"

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

sty/Test4DT_tests/test_sty_primitive_Register___call___2_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

custom_register = <sty.primitive.Register object at 0x10645ee30>

    def test_valid_inputs(custom_register):
        # Test setting 8-bit color code
>       assert custom_register(42) == "42"
E       AssertionError: assert 42 == '42'
E        +  where 42 = <sty.primitive.Register object at 0x10645ee30>(42)

sty/Test4DT_tests/test_sty_primitive_Register___call___2_test_valid_inputs.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register___call___2_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.02s ===============================
"""