
import pytest
from thefuck.types import Rule

def test_invalid_input():
    with pytest.raises(Exception):
        rule = Rule()  # This should raise an Exception because __init__ requires parameters
