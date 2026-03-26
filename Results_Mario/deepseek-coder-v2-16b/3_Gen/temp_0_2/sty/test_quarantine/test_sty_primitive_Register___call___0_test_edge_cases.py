
import pytest
from sty import Register

def test_edge_cases():
    custom_register = Register()
    
    # Test None input
    with pytest.raises(TypeError):
        assert custom_register(None)
    
    # Test empty list input
    with pytest.raises(TypeError):
        assert custom_register([])
    
    # Test invalid color code (non-integer for 8-bit call)
    with pytest.raises(TypeError):
        assert custom_register('invalid')
    
    # Test invalid attribute name
    with pytest.raises(AttributeError):
        assert custom_register('nonexistent_attribute')

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
        with pytest.raises(TypeError):
            assert custom_register(None)
    
        # Test empty list input
        with pytest.raises(TypeError):
            assert custom_register([])
    
        # Test invalid color code (non-integer for 8-bit call)
        with pytest.raises(TypeError):
>           assert custom_register('invalid')

sty/Test4DT_tests/test_sty_primitive_Register___call___0_test_edge_cases.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <sty.primitive.Register object at 0x1039f8520>, args = ('invalid',)
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
E               AttributeError: 'Register' object has no attribute 'invalid'

sty/sty/primitive.py:107: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register___call___0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.02s ===============================
"""