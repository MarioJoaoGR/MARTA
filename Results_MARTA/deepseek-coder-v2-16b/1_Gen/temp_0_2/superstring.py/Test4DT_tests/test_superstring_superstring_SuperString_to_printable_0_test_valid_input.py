
import pytest
from superstring.superstring import SuperString

def test_valid_input():
    s = SuperString('Hello, World!')
    assert s.to_printable(0, 5) == 'Hello'
    assert s.to_printable(7, 12) == 'World'
    assert s.to_printable(0, 13) == 'Hello, World!'
    assert s.to_printable(0, len('Hello, World!')) == 'Hello, World!'
