
import pytest
from sty.primitive import Register, RenderType

def test_valid_input():
    reg = Register()
    
    # Mock a valid render type for testing
    class ValidRenderType:
        def __call__(self, *args):
            return "Valid Eightbit Call"
    
    # Assign the mock to the register's renderfuncs dictionary
    reg.renderfuncs['valid_type'] = ValidRenderType()
    
    # Set the valid render type for eightbit call
    reg.set_eightbit_call(ValidRenderType)
    
    # Assert that the eightbit_call is set to the mock function
    assert callable(reg.eightbit_call)
    assert reg.eightbit_call.__name__ == "valid_type"

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

sty/Test4DT_tests/test_sty_primitive_Register_set_eightbit_call_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        reg = Register()
    
        # Mock a valid render type for testing
        class ValidRenderType:
            def __call__(self, *args):
                return "Valid Eightbit Call"
    
        # Assign the mock to the register's renderfuncs dictionary
        reg.renderfuncs['valid_type'] = ValidRenderType()
    
        # Set the valid render type for eightbit call
>       reg.set_eightbit_call(ValidRenderType)

sty/Test4DT_tests/test_sty_primitive_Register_set_eightbit_call_0_test_valid_input.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <sty.primitive.Register object at 0x103dd0880>
rendertype = <class 'Test4DT_tests.test_sty_primitive_Register_set_eightbit_call_0_test_valid_input.test_valid_input.<locals>.ValidRenderType'>

    def set_eightbit_call(self, rendertype: Type[RenderType]) -> None:
        """
        You can call a register-object directly. A call like this ``fg(144)``
        is a Eightbit-call. With this method you can define the render-type for such calls.
    
        :param rendertype: The new rendertype that is used for Eightbit-calls.
        """
>       func: Callable = self.renderfuncs[rendertype]
E       KeyError: <class 'Test4DT_tests.test_sty_primitive_Register_set_eightbit_call_0_test_valid_input.test_valid_input.<locals>.ValidRenderType'>

sty/sty/primitive.py:123: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register_set_eightbit_call_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.02s ===============================
"""