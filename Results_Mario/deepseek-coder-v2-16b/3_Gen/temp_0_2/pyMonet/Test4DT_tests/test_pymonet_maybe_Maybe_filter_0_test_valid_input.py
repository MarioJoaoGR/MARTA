
import pytest
from pymonet.maybe import Maybe

def test_valid_input():
    maybe_some = Maybe(value=42, is_nothing=False)
    filtered_maybe = maybe_some.filter(lambda x: x > 10)
    assert not filtered_maybe.is_nothing
    assert filtered_maybe.value == 42
