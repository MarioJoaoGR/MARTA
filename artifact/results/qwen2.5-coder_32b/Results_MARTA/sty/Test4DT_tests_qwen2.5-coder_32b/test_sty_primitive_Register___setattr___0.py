
import pytest
from sty.primitive import Register, Style



def test_register_setattr_with_non_style():
    # Arrange
    register = Register()
    non_style_value = "some_string"
    
    # Act
    register.some_attribute = non_style_value
    
    # Assert
    assert register.some_attribute == non_style_value

# Assuming _render_rules is a function that needs to be tested separately or is correctly implemented.

# Assuming Style and StylingRule are correctly defined in sty.primitive