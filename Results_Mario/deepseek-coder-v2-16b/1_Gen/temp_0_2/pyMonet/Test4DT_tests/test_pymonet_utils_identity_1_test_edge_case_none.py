
import pytest
from pymonet.utils import identity  # Assuming this module exists in your project structure

def test_identity():
    assert identity(None) is None
    assert identity(0) == 0
    assert identity("") == ""
    assert identity([]) == []
    assert identity({}) == {}
