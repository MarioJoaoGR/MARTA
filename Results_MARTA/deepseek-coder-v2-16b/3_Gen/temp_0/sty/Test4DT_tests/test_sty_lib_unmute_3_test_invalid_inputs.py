
import pytest
from sty.lib import Register

class MockInvalid(object): pass

def unmute(*objects: Register) -> None:
    err = ValueError(
        "The unmute() method can only be used with objects that inherit "
        "from the 'Register class'."
    )
    for obj in objects:
        if not isinstance(obj, Register):
            raise err
        obj.unmute()

def test_invalid_inputs():
    obj1 = MockInvalid()
    obj2 = MockInvalid()
    
    with pytest.raises(ValueError) as excinfo:
        unmute(obj1, obj2)
    
    assert str(excinfo.value) == "The unmute() method can only be used with objects that inherit from the 'Register class'."
