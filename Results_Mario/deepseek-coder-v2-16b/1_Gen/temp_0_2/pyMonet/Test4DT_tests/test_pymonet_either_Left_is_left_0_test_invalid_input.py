
from pymonet.either import Left

def test_invalid_input():
    try:
        Left(value=None)  # This should raise a TypeError because Left does not accept 'value' as an argument
    except TypeError as e:
        assert str(e) == "__init__() got an unexpected keyword argument 'value'"
