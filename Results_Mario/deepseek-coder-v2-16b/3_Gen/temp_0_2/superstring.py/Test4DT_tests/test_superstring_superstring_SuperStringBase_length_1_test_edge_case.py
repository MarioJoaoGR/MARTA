
from superstring.superstring import SuperStringBase
import pytest

class MyString(SuperStringBase):
    def __init__(self, value):
        self.value = value
    
    def length(self):
        return len(self.value)

def test_edge_case():
    my_string = MyString("")
    assert my_string.length() == 0
