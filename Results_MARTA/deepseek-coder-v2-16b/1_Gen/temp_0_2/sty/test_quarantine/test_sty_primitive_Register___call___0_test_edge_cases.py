
import pytest
from sty.primitive import Register

def test_edge_cases():
    custom_register = Register()
    
    # Test None input
    assert custom_register(None) == ""

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

sty/Test4DT_tests/test_sty_primitive_Register___call___0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        custom_register = Register()
    
        # Test None input
>       assert custom_register(None) == ""

sty/Test4DT_tests/test_sty_primitive_Register___call___0_test_edge_cases.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <sty.primitive.Register object at 0x106a8d330>, args = (None,)
kwargs = {}, len_args = 1

    def __call__(self, *args: Union[int, str], **kwargs) -> str:
        """
        This function is to handle calls such as `fg(42)`, `bg(102, 49, 42)`, `fg('red')`.
        """
    
        # Return empty str if object is muted.
        if self.is_muted:
            return ""
    
        len_args = len(args)
    
        if len_args == 1:
            # If input is an 8bit color code, run 8bit render function.
            if isinstance(args[0], int):
                return self.eightbit_call(*args, **kwargs)
    
            # If input is a string, return attribute with the name that matches
            # input.
            else:
>               return getattr(self, args[0])
E               TypeError: getattr(): attribute name must be string

sty/sty/primitive.py:107: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register___call___0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.02s ===============================
"""