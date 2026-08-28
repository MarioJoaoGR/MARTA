
# Module: sty.primitive
import pytest
from sty.primitive import Register

class MockStyle:
    def __init__(self):
        self.rules = ["some_rule"]
        self.value = ""

def test_register_mute_with_style_attribute():
    register = Register()
    
    # Set a Style attribute
    style_instance = MockStyle()
    register.some_style = style_instance
    
    # Ensure the initial state is correct
    assert not register.is_muted, "is_muted should be False by default"
    assert isinstance(register.some_style, MockStyle), "some_style should be an instance of MockStyle"
    
    # Call mute method
    register.mute()
    
    # Verify that is_muted is set to True
    assert register.is_muted, "is_muted should be True after calling mute"
    
    # Verify that the Style attribute remains an instance of MockStyle
    assert isinstance(register.some_style, MockStyle), "Muting should not change the type of Style attributes"

def test_register_mute_with_multiple_style_attributes():
    register = Register()
    
    # Set multiple Style attributes
    style_instance1 = MockStyle()
    style_instance2 = MockStyle()
    register.style1 = style_instance1
    register.style2 = style_instance2
    
    # Ensure the initial state is correct
    assert not register.is_muted, "is_muted should be False by default"
    assert isinstance(register.style1, MockStyle), "style1 should be an instance of MockStyle"
    assert isinstance(register.style2, MockStyle), "style2 should be an instance of MockStyle"
    
    # Call mute method
    register.mute()
    
    # Verify that is_muted is set to True
    assert register.is_muted, "is_muted should be True after calling mute"
    
    # Verify that the Style attributes remain instances of MockStyle
    assert isinstance(register.style1, MockStyle), "Muting should not change the type of style1 attribute"
    assert isinstance(register.style2, MockStyle), "Muting should not change the type of style2 attribute"

def test_register_mute_with_no_style_attributes():
    register = Register()
    
    # Ensure there are no Style attributes
    assert not any(isinstance(getattr(register, attr_name), MockStyle) for attr_name in dir(register)), "No Style attributes should be present initially"
    
    # Call mute method
    register.mute()
    
    # Verify that is_muted is set to True
    assert register.is_muted, "is_muted should be True after calling mute"

def test_register_mute_with_non_style_attributes():
    register = Register()
    
    # Set non-Style attributes
    register.non_style_attr1 = "some_value"
    register.non_style_attr2 = 42
    
    # Ensure the initial state is correct
    assert not register.is_muted, "is_muted should be False by default"
    assert register.non_style_attr1 == "some_value", "non_style_attr1 should have the set value"
    assert register.non_style_attr2 == 42, "non_style_attr2 should have the set value"
    
    # Call mute method
    register.mute()
    
    # Verify that is_muted is set to True
    assert register.is_muted, "is_muted should be True after calling mute"
    
    # Verify that non-Style attributes remain unchanged
    assert register.non_style_attr1 == "some_value", "non_style_attr1 should remain unchanged"
    assert register.non_style_attr2 == 42, "non_style_attr2 should remain unchanged"

def test_register_mute_with_mixed_attributes():
    register = Register()
    
    # Set a Style attribute
    style_instance = MockStyle()
    register.some_style = style_instance
    
    # Set non-Style attributes
    register.non_style_attr1 = "some_value"
    register.non_style_attr2 = 42
    
    # Ensure the initial state is correct
    assert not register.is_muted, "is_muted should be False by default"
    assert isinstance(register.some_style, MockStyle), "some_style should be an instance of MockStyle"
    assert register.non_style_attr1 == "some_value", "non_style_attr1 should have the set value"
    assert register.non_style_attr2 == 42, "non_style_attr2 should have the set value"
    
    # Call mute method
    register.mute()
    
    # Verify that is_muted is set to True
    assert register.is_muted, "is_muted should be True after calling mute"
    
    # Verify that the Style attribute remains an instance of MockStyle
    assert isinstance(register.some_style, MockStyle), "Muting should not change the type of some_style attribute"
    
    # Verify that non-Style attributes remain unchanged
    assert register.non_style_attr1 == "some_value", "non_style_attr1 should remain unchanged"
    assert register.non_style_attr2 == 42, "non_style_attr2 should remain unchanged"

