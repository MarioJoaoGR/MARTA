
import pytest
from sty import primitive

class Register:
    """
    This is the base Register class. All default registers (fg, bg, ef, rs) are created from this class. You can use it to create your own custom registers.
    
    Attributes:
        renderfuncs (Renderfuncs): A dictionary containing rendering functions for various color formats.
        is_muted (bool): Indicates whether the register is muted.
        eightbit_call (lambda): A lambda function that takes an integer and returns its 8-bit representation.
        rgb_call (lambda): A lambda function that takes three integers (red, green, blue) and returns a tuple of these values in RGB format.
    
    Methods:
        as_dict() -> Dict[str, str]:
            Export color register as dict.
            
            Returns:
                items (Dict[str, str]): A dictionary containing the names and string representations of all attributes that start with an underscore.
                
        as_namedtuple(self) -> namedtuple:
            Export color register as namedtuple.
            
            This method converts the color register stored in the instance to a namedtuple, where keys from the dictionary representation of the register are used as field names.
            
            Returns:
                namedtuple: A namedtuple representing the color register.
    """
    def __init__(self):
        self.renderfuncs = {}
        self.is_muted = False
        self.eightbit_call = lambda x: x
        self.rgb_call = lambda r, g, b: (r, g, b)

    def as_dict(self) -> dict:
        """
        Export color register as dict.
        """
        items = {}
        for name in dir(self):
            if not name.startswith("_") and isinstance(getattr(self, name), str):
                items[name] = str(getattr(self, name))
        return items

@pytest.fixture
def custom_register():
    return Register()

def test_valid_case(custom_register):
    # Test that the as_dict method returns a dictionary with string representations of attributes starting with an underscore
    result = custom_register.as_dict()
    assert isinstance(result, dict)
    for key in result:
        assert str(getattr(custom_register, key)).startswith("_")
