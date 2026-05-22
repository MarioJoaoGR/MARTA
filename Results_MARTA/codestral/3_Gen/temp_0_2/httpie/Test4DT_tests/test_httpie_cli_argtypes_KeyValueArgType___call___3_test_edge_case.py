
import pytest
from argparse import ArgumentTypeError
from httpie.cli.argtypes import KeyValueArgType

@pytest.fixture(scope="function")
def kvat():
    return KeyValueArgType('=')

def test_edge_case(kvat):
    with pytest.raises(ArgumentTypeError) as excinfo:
        kvat("")
    assert str(excinfo.value) == "'' is not a valid value"
