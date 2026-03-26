
import pytest
from sty.primitive import Register

@pytest.fixture
def custom_register():
    return Register()

def test_valid_inputs(custom_register):
    # Modify the attributes to have string values for testing
    custom_register.renderfuncs['test'] = 'test_value'
    custom_register.is_muted = True
    custom_register.eightbit_call = lambda x: f"8-bit({x})"
    custom_register.rgb_call = lambda r, g, b: f"RGB({r}, {g}, {b})"
    
    # Call the as_dict method and check the output
    result = custom_register.as_dict()
    assert isinstance(result, dict)
    assert 'renderfuncs' in result

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

sty/Test4DT_tests/test_sty_primitive_Register_as_dict_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

custom_register = <sty.primitive.Register object at 0x104428d00>

    def test_valid_inputs(custom_register):
        # Modify the attributes to have string values for testing
        custom_register.renderfuncs['test'] = 'test_value'
        custom_register.is_muted = True
        custom_register.eightbit_call = lambda x: f"8-bit({x})"
        custom_register.rgb_call = lambda r, g, b: f"RGB({r}, {g}, {b})"
    
        # Call the as_dict method and check the output
        result = custom_register.as_dict()
        assert isinstance(result, dict)
>       assert 'renderfuncs' in result
E       AssertionError: assert 'renderfuncs' in {}

sty/Test4DT_tests/test_sty_primitive_Register_as_dict_0_test_valid_inputs.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register_as_dict_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.03s ===============================
"""