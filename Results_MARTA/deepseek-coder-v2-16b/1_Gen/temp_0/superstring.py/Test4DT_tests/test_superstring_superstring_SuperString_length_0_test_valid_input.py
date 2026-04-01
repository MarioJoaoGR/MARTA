
from superstring.superstring import SuperString

def test_valid_input():
    s = SuperString("Hello, world!")
    
    # Test substring method with default end index
    assert str(s.substring(0)) == "Hello, world!"
