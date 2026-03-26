
import pytest
from superstring.superstring import SuperStringBase

class ConcreteSuperString(SuperStringBase):
    def __init__(self, string):
        self.string = string
    
    def length(self):
        return len(self.string)

def test_invalid_input():
    with pytest.raises(TypeError):
        concrete_instance = ConcreteSuperString(12345)  # Invalid input type (int instead of str)
        concrete_instance.length()
