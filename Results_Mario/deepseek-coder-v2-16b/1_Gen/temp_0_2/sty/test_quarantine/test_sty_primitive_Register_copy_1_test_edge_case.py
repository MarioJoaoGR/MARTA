
import pytest
from copy import deepcopy
from sty.primitive import Register

def test_edge_case():
    # Create an instance of Register
    reg = Register()
    
    # Make a copy of the register
    copied_reg = reg.copy()
    
    # Check if the copied register is not muted and has the same RGB call lambda function
    assert not reg.is_muted == copied_reg.is_muted

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

sty/Test4DT_tests/test_sty_primitive_Register_copy_1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        # Create an instance of Register
        reg = Register()
    
        # Make a copy of the register
        copied_reg = reg.copy()
    
        # Check if the copied register is not muted and has the same RGB call lambda function
>       assert not reg.is_muted == copied_reg.is_muted
E       assert not False == False
E        +  where False = <sty.primitive.Register object at 0x1044214e0>.is_muted
E        +  and   False = <sty.primitive.Register object at 0x1044213c0>.is_muted

sty/Test4DT_tests/test_sty_primitive_Register_copy_1_test_edge_case.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register_copy_1_test_edge_case.py::test_edge_case
============================== 1 failed in 0.02s ===============================
"""