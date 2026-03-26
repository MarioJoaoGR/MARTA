
import pytest
from sty.primitive import Register

def test_invalid_inputs():
    custom_register = Register()
    
    # Test with invalid input (non-string values)
    for attr in ['renderfuncs', 'is_muted', 'eightbit_call', 'rgb_call']:
        with pytest.raises(TypeError):
            if attr == 'renderfuncs':
                setattr(custom_register, attr, 12345)  # Invalid type for renderfuncs
            elif attr == 'is_muted':
                setattr(custom_register, attr, "not a bool")  # Invalid type for is_muted
            elif attr == 'eightbit_call':
                setattr(custom_register, attr, "not a lambda function")  # Invalid type for eightbit_call
            elif attr == 'rgb_call':
                setattr(custom_register, attr, "not a lambda function")  # Invalid type for rgb_call

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

sty/Test4DT_tests/test_sty_primitive_Register_as_dict_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        custom_register = Register()
    
        # Test with invalid input (non-string values)
        for attr in ['renderfuncs', 'is_muted', 'eightbit_call', 'rgb_call']:
>           with pytest.raises(TypeError):
E           Failed: DID NOT RAISE <class 'TypeError'>

sty/Test4DT_tests/test_sty_primitive_Register_as_dict_0_test_invalid_inputs.py:10: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register_as_dict_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.03s ===============================
"""