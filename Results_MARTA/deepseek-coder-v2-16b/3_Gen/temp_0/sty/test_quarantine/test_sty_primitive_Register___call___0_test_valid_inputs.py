
import pytest
from sty import primitive

@pytest.fixture(scope="module")
def reg():
    return primitive.Register()

def test_valid_inputs(reg):
    # Test setting fg to an 8-bit color code
    assert reg(fg=42) == ""
    
    # Test setting bg to a 24-bit RGB color
    assert reg(bg=(102, 49, 42)) == (102, 49, 42)
    
    # Test setting fg to a named color
    assert reg(fg='red') == ""

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

reg = <sty.primitive.Register object at 0x1020975b0>

    def test_valid_inputs(reg):
        # Test setting fg to an 8-bit color code
        assert reg(fg=42) == ""
    
        # Test setting bg to a 24-bit RGB color
>       assert reg(bg=(102, 49, 42)) == (102, 49, 42)
E       AssertionError: assert '' == (102, 49, 42)
E        +  where '' = <sty.primitive.Register object at 0x1020975b0>(bg=(102, 49, 42))

sty/Test4DT_tests/test_sty_primitive_Register___call___0_test_valid_inputs.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register___call___0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.02s ===============================
"""