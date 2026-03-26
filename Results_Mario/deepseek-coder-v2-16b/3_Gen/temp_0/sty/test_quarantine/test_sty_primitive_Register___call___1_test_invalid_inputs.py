
import pytest
from sty import primitive

@pytest.fixture(scope="module")
def reg():
    return primitive.Register()

def test_invalid_inputs(reg):
    with pytest.raises(TypeError):
        # Test invalid input type for fg
        assert reg(fg=None) == ""
        
        # Test invalid input type for bg
        assert reg(bg=(256, 0, 0)) == ""
        
        # Test invalid input type for fg as string with invalid name
        assert reg(fg="invalid_color") == ""
        
        # Test invalid number of arguments for fg and bg
        with pytest.raises(TypeError):
            reg(fg=42, bg=102)
            
        # Test valid input types for fg and bg
        assert reg(fg=42) == "Custom 42"
        assert reg(bg=(102, 49, 42)) == (102, 49, 42)
        
        # Test valid input type for fg as string with valid name
        assert reg(fg="red") == "Custom red"

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

reg = <sty.primitive.Register object at 0x104816920>

    def test_invalid_inputs(reg):
        with pytest.raises(TypeError):
            # Test invalid input type for fg
            assert reg(fg=None) == ""
    
            # Test invalid input type for bg
            assert reg(bg=(256, 0, 0)) == ""
    
            # Test invalid input type for fg as string with invalid name
            assert reg(fg="invalid_color") == ""
    
            # Test invalid number of arguments for fg and bg
>           with pytest.raises(TypeError):
E           Failed: DID NOT RAISE <class 'TypeError'>

sty/Test4DT_tests/test_sty_primitive_Register___call___1_test_invalid_inputs.py:21: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register___call___1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.02s ===============================
"""