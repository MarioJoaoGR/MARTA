
import pytest
from sty import primitive

class TestRegisterSetEightbitCall2InvalidInput:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        self.reg = primitive.Register()
    
    def test_invalid_input(self):
        with pytest.raises(TypeError):
            self.reg.set_eightbit_call("InvalidType")

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

sty/Test4DT_tests/test_sty_primitive_Register_set_eightbit_call_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
_________ TestRegisterSetEightbitCall2InvalidInput.test_invalid_input __________

self = <Test4DT_tests.test_sty_primitive_Register_set_eightbit_call_2_test_invalid_input.TestRegisterSetEightbitCall2InvalidInput object at 0x102251600>

    def test_invalid_input(self):
        with pytest.raises(TypeError):
>           self.reg.set_eightbit_call("InvalidType")

sty/Test4DT_tests/test_sty_primitive_Register_set_eightbit_call_2_test_invalid_input.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <sty.primitive.Register object at 0x1022517b0>
rendertype = 'InvalidType'

    def set_eightbit_call(self, rendertype: Type[RenderType]) -> None:
        """
        You can call a register-object directly. A call like this ``fg(144)``
        is a Eightbit-call. With this method you can define the render-type for such calls.
    
        :param rendertype: The new rendertype that is used for Eightbit-calls.
        """
>       func: Callable = self.renderfuncs[rendertype]
E       KeyError: 'InvalidType'

sty/sty/primitive.py:123: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register_set_eightbit_call_2_test_invalid_input.py::TestRegisterSetEightbitCall2InvalidInput::test_invalid_input
============================== 1 failed in 0.02s ===============================
"""