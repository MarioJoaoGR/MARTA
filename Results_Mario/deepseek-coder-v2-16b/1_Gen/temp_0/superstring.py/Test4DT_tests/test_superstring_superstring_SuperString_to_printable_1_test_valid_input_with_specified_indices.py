
from superstring.superstring import SuperString

def test_valid_input_with_specified_indices():
    s = SuperString('Hello, World!')
    
    # Test substring from start index to the end of the string
    assert s.to_printable(0) == 'Hello, World!'
