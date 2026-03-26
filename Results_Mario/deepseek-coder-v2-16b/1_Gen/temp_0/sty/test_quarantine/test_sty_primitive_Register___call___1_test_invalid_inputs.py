
import pytest
from sty.primitive import Register

@pytest.fixture(name="reg")
def fixture_register():
    return Register()

def test_invalid_inputs(reg):
    # Test invalid inputs by calling the __call__ method with different types of arguments
    
    # Invalid: No arguments provided
    assert reg() == ""
    
    # Invalid: Too many arguments (more than 3)
    with pytest.raises(TypeError):
        reg(1, 2, 3, 4)
    
    # Invalid: Argument is neither int nor str for single argument case
    with pytest.raises(AttributeError):
        reg("invalid_attribute")

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

sty/Test4DT_tests/test_sty_primitive_Register___call___1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

reg = <sty.primitive.Register object at 0x101991fc0>

    def test_invalid_inputs(reg):
        # Test invalid inputs by calling the __call__ method with different types of arguments
    
        # Invalid: No arguments provided
        assert reg() == ""
    
        # Invalid: Too many arguments (more than 3)
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

sty/Test4DT_tests/test_sty_primitive_Register___call___1_test_invalid_inputs.py:16: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register___call___1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.02s ===============================

"""