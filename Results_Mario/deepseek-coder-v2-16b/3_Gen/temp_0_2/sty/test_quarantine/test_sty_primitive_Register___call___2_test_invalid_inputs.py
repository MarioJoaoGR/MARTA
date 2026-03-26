
import pytest
from sty.primitive import Register

@pytest.fixture(name="custom_register")
def create_custom_register():
    return Register()

def test_invalid_inputs(custom_register):
    # Test that calling with invalid inputs returns an empty string
    assert custom_register("invalid_input") == ""
    assert custom_register(12345) == ""  # Assuming eightbit_call always returns "", replace if implementation changes
    assert custom_register(102, 49, 42) == (102, 49, 42)  # Assuming rgb_call returns a tuple of RGB values

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

sty/Test4DT_tests/test_sty_primitive_Register___call___2_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

custom_register = <sty.primitive.Register object at 0x105bbf5b0>

    def test_invalid_inputs(custom_register):
        # Test that calling with invalid inputs returns an empty string
>       assert custom_register("invalid_input") == ""

sty/Test4DT_tests/test_sty_primitive_Register___call___2_test_invalid_inputs.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <sty.primitive.Register object at 0x105bbf5b0>, args = ('invalid_input',)
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
E               AttributeError: 'Register' object has no attribute 'invalid_input'

sty/sty/primitive.py:107: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register___call___2_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.02s ===============================
"""