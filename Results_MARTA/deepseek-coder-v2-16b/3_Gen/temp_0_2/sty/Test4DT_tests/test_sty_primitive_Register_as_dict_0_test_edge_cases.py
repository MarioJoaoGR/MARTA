
# Importing the Register class from the correct module
from sty.primitive import Register

def test_edge_cases():
    # Creating an instance of the Register class
    register = Register()
    
    # Calling the as_dict method to get the dictionary representation of the color registers
    register_dict = register.as_dict()
    
    # Asserting that the output is a dictionary (even if it's empty, it should be a dictionary)
    assert isinstance(register_dict, dict), "The result should be a dictionary"
