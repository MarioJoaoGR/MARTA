
import pytest
from sty.primitive import Register

def test_error_case():
    # Create an instance of the Register class
    reg = Register()
    
    # Call the as_namedtuple method to convert it to a namedtuple
    nt = reg.as_namedtuple()
    
    # Check if the result is a namedtuple with the expected keys and values
    assert isinstance(nt, tuple)
    assert len(nt._fields) == 4  # Assuming there are four fields as in the example

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

sty/Test4DT_tests/test_sty_primitive_Register_as_namedtuple_1_test_error_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_error_case ________________________________

    def test_error_case():
        # Create an instance of the Register class
        reg = Register()
    
        # Call the as_namedtuple method to convert it to a namedtuple
        nt = reg.as_namedtuple()
    
        # Check if the result is a namedtuple with the expected keys and values
        assert isinstance(nt, tuple)
>       assert len(nt._fields) == 4  # Assuming there are four fields as in the example
E       assert 0 == 4
E        +  where 0 = len(())
E        +    where () = StyleRegister()._fields

sty/Test4DT_tests/test_sty_primitive_Register_as_namedtuple_1_test_error_case.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register_as_namedtuple_1_test_error_case.py::test_error_case
============================== 1 failed in 0.02s ===============================
"""