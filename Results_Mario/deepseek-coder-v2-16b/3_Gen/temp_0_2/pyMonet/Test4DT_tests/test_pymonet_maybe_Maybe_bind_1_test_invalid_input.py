
import pytest
from pymonet.maybe import Maybe

def test_invalid_input():
    maybe_some = Maybe(value=42, is_nothing=False)
    with pytest.raises(TypeError):
        maybe_some.bind("not a callable")
