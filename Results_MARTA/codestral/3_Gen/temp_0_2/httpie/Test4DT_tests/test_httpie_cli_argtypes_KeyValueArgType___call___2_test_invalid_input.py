
import pytest
from argparse import ArgumentTypeError
from httpie.cli.argtypes import KeyValueArgType

def test_invalid_input():
    kvat = KeyValueArgType('=')
    
    with pytest.raises(ArgumentTypeError):
        kvat("invalid input")
