
import pytest
from argparse import ArgumentTypeError
from httpie.cli.argtypes import KeyValueArgType

def test_invalid_input_error_handling():
    key_value_parser = KeyValueArgType()
    
    with pytest.raises(ArgumentTypeError):
        key_value_parser("invalid input")
