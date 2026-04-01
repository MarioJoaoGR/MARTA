
from pymonet.maybe import Maybe
from pymonet.box import Box

def test_valid_input():
    # Test when Maybe is not nothing (is_nothing is False)
    maybe = Maybe(value=42, is_nothing=False)
    assert isinstance(maybe.to_box(), Box)
    assert maybe.to_box().value == 42

    # Test when Maybe is nothing (is_nothing is True)
    maybe_nothing = Maybe(value=None, is_nothing=True)
    assert isinstance(maybe_nothing.to_box(), Box)
    assert maybe_nothing.to_box().value is None
