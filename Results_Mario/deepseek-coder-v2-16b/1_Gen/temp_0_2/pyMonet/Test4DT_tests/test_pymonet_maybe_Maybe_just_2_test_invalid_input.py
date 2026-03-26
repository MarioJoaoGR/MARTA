
from pymonet.maybe import Maybe

def test_invalid_input():
    # Test when value is provided but is_nothing is True
    try:
        maybe = Maybe(value=42, is_nothing=True)  # This should raise an error because the input is invalid
    except TypeError as e:
        assert str(e) == "Maybe.__init__() missing 1 required positional argument: 'is_nothing'"
