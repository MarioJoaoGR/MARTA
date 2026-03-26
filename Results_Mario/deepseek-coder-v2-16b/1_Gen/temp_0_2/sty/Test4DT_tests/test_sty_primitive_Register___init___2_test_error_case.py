
# Importing the Register class from the correct module
from sty.primitive import Register

def test_error_case():
    # Creating an instance of Register to use in the test
    register = Register()
    
    # Adding assertions or checks if necessary to verify the functionality
    assert register is not None, "Register instance should be created successfully"
