
from sty.primitive import Renderfuncs  # Importing from the correct module

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
        self.renderfuncs: Renderfuncs = {}  # Correctly referencing the imported type
        self.is_muted = False
        self.eightbit_call = lambda x: x
        self.rgb_call = lambda r, g, b: (r, g, b)

    def as_namedtuple(self):
        """
        Export color register as namedtuple.
        """
        d = self.as_dict()
        return namedtuple("StyleRegister", d.keys())(*d.values())

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_primitive_Register_as_namedtuple_1_test_edge_case
sty/Test4DT_tests/test_sty_primitive_Register_as_namedtuple_1_test_edge_case.py:31:12: E1101: Instance of 'Register' has no 'as_dict' member (no-member)
sty/Test4DT_tests/test_sty_primitive_Register_as_namedtuple_1_test_edge_case.py:32:15: E0602: Undefined variable 'namedtuple' (undefined-variable)


"""