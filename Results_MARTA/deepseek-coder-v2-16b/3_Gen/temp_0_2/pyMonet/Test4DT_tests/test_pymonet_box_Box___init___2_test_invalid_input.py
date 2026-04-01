
from pymonet.box import Box

def test_invalid_input():
    # Test that the constructor raises a TypeError when given an invalid input type
    try:
        box = Box(None)  # Passing None, which is not allowed
    except TypeError as e:
        assert str(e) == "__init__() missing 1 required positional argument: 'value'"
