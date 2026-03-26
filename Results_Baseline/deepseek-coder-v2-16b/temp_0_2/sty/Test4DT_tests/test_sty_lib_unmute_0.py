# Module: sty.lib
import pytest
from sty.lib import unmute, Register

# Test fixture to create a dummy subclass of Register for testing purposes
@pytest.fixture
def register_objects():
    class SubRegister(Register):
        pass
    
    obj1 = Register()
    obj2 = SubRegister()
    return obj1, obj2

def test_unmute_multiple_registers(register_objects):
    obj1, obj2 = register_objects
    unmute(obj1, obj2)
    assert not obj1.is_muted
    assert not obj2.is_muted

def test_unmute_single_register():
    obj = Register()
    unmute(obj)
    assert not obj.is_muted

def test_unmute_invalid_object():
    class NotARegister:
        pass
    
    obj1 = Register()
    obj2 = NotARegister()
    with pytest.raises(ValueError, match="The unmute\(\) method can only be used with objects that inherit from the 'Register class'."):
        unmute(obj1, obj2)
