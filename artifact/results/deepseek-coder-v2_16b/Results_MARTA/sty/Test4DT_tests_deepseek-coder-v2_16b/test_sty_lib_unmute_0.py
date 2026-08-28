
import pytest
from sty.lib import Register, unmute

def test_unmute_valid_objects():
    class MockRegister(Register):
        def __init__(self):
            self.muted = True
        
        def unmute(self):
            self.muted = False
    
    register1 = MockRegister()
    register2 = MockRegister()
    
    unmute(register1, register2)
    
    assert not register1.muted
    assert not register2.muted

def test_unmute_invalid_objects():
    class InvalidObject:
        pass
    
    invalid_obj = InvalidObject()
    
    with pytest.raises(ValueError):
        unmute(invalid_obj)
