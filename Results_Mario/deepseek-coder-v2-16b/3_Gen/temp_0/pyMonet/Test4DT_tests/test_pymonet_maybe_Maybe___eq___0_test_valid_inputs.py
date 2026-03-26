
import pytest
from pymonet.maybe import Maybe

def test_valid_inputs():
    maybe_some = Maybe(10, False)
    maybe_none = Maybe(None, True)
    
    assert maybe_some == Maybe(10, False)
    assert not (maybe_some == maybe_none)
    assert maybe_none == Maybe(None, True)
