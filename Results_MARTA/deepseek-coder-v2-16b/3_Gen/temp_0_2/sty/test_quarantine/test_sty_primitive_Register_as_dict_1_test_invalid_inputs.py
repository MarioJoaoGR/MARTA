
import pytest
from sty import primitive

class Register:
    """
    The base Register class from which default registers such as fg, bg, ef, and rs are created. This class can be used to create custom registers.
    
    Attributes:
        renderfuncs (Renderfuncs): A dictionary containing rendering functions for the register.
        is_muted (bool): Indicates whether the register is muted.
        eightbit_call (lambda): A lambda function that takes one argument and returns it.
        rgb_call (lambda): A lambda function that takes three arguments (red, green, blue) and returns a tuple of these values.
    
    Examples:
        To create a custom register, you can instantiate the Register class::
        
            custom_register = Register()
            
        You can then use this custom register for various purposes in your application.
    """
    def __init__(self):
        self.renderfuncs: Renderfuncs = {}
        self.is_muted = False
        self.eightbit_call = lambda x: x
        self.rgb_call = lambda r, g, b: (r, g, b)

    def as_dict(self) -> Dict[str, str]:
        """
        Export color register as dict.
        """
        items: Dict[str, str] = {}

        for name in dir(self):
            if not name.startswith("_") and isinstance(getattr(self, name), str):
                items.update({name: str(getattr(self, name))})

        return items

def test_invalid_inputs():
    register = Register()
    
    # Test with invalid input types (non-string values)
    with pytest.raises(TypeError):
        class InvalidTypeRegister(Register):
            def __init__(self):
                super().__init__()
                self.invalid_attr = 12345  # This should raise a TypeError when calling as_dict
        
        invalid_register = InvalidTypeRegister()
        invalid_register.as_dict()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_primitive_Register_as_dict_1_test_invalid_inputs
sty/Test4DT_tests/test_sty_primitive_Register_as_dict_1_test_invalid_inputs.py:23:26: E0602: Undefined variable 'Renderfuncs' (undefined-variable)
sty/Test4DT_tests/test_sty_primitive_Register_as_dict_1_test_invalid_inputs.py:28:25: E0602: Undefined variable 'Dict' (undefined-variable)
sty/Test4DT_tests/test_sty_primitive_Register_as_dict_1_test_invalid_inputs.py:32:15: E0602: Undefined variable 'Dict' (undefined-variable)


"""