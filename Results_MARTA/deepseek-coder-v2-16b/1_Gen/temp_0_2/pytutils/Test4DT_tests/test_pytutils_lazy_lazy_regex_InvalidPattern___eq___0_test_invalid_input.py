
import pytest
from pytutils.lazy.lazy_regex import InvalidPattern

def test_invalid_input():
    with pytest.raises(InvalidPattern):
        raise InvalidPattern("This is an example of an invalid pattern.")
