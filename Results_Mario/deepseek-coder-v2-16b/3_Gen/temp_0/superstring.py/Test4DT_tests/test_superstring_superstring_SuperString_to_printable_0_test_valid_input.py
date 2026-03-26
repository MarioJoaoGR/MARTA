
import pytest
from superstring import SuperString

def test_valid_input():
    s = SuperString('Hello, World!')
    assert s.to_printable(0) == 'Hello, World!'
    assert s.to_printable(7, 12) == 'World'
