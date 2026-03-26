
import pytest
from sty.primitive import Register, Renderfuncs  # Assuming this is the correct module path

def test_set_rgb_call_invalid_input():
    reg = Register()
    
    with pytest.raises(TypeError):
        reg.set_rgb_call("InvalidType")

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

sty/Test4DT_tests/test_sty_primitive_Register_set_rgb_call_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
_______________________ test_set_rgb_call_invalid_input ________________________

    def test_set_rgb_call_invalid_input():
        reg = Register()
    
        with pytest.raises(TypeError):
>           reg.set_rgb_call("InvalidType")

sty/Test4DT_tests/test_sty_primitive_Register_set_rgb_call_1_test_invalid_input.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <sty.primitive.Register object at 0x105c698d0>
rendertype = 'InvalidType'

    def set_rgb_call(self, rendertype: Type[RenderType]) -> None:
        """
        You can call a register-object directly. A call like this ``fg(10, 42, 255)``
        is a RGB-call. With this method you can define the render-type for such calls.
    
        :param rendertype: The new rendertype that is used for RGB-calls.
        """
>       func: Callable = self.renderfuncs[rendertype]
E       KeyError: 'InvalidType'

sty/sty/primitive.py:133: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register_set_rgb_call_1_test_invalid_input.py::test_set_rgb_call_invalid_input
============================== 1 failed in 0.02s ===============================
"""