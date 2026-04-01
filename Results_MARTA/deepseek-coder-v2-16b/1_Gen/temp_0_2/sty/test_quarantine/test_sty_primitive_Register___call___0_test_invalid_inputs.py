
import pytest
from sty import primitive

def test_invalid_inputs():
    custom_register = primitive.Register()
    
    # Test with no arguments
    assert custom_register() == ""
    
    # Test with one invalid argument (not an int or str)
    with pytest.raises(AttributeError):
        custom_register("invalid_arg")
    
    # Test with two arguments (should raise TypeError)
    with pytest.raises(TypeError):
        custom_register(1, 2)

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

sty/Test4DT_tests/test_sty_primitive_Register___call___0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        custom_register = primitive.Register()
    
        # Test with no arguments
        assert custom_register() == ""
    
        # Test with one invalid argument (not an int or str)
        with pytest.raises(AttributeError):
            custom_register("invalid_arg")
    
        # Test with two arguments (should raise TypeError)
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

sty/Test4DT_tests/test_sty_primitive_Register___call___0_test_invalid_inputs.py:16: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register___call___0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.03s ===============================
"""