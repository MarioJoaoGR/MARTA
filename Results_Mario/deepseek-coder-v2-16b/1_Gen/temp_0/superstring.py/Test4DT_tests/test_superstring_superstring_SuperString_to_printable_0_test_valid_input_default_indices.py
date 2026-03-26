
import pytest
from superstring import SuperString

def test_valid_input_default_indices():
    s = SuperString('Hello, World!')
    assert s.to_printable() == 'Hello, World!'
