
import pytest
from sty.lib import Register, unmute

class AnotherRegisterSubclass(Register):
    def unmute(self):
        pass

def test_valid_input():
    obj1 = Register()
    obj2 = AnotherRegisterSubclass()
    unmute(obj1, obj2)  # This should not raise an error since both objects are valid inputs
