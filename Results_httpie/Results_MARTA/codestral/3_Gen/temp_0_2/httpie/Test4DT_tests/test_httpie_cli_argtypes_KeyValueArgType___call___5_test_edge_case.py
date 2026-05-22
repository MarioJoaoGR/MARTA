
import pytest
from argparse import ArgumentTypeError
from httpie.cli.argtypes import KeyValueArgType

def test_edge_case():
    kvat = KeyValueArgType('=')
    
    with pytest.raises(ArgumentTypeError):
        kvat("")
