
import pytest
from argparse import ArgumentTypeError
from httpie.cli.argtypes import KeyValueArgType

@pytest.fixture(scope="function")
def kvat():
    return KeyValueArgType('=')

def test_valid_input(kvat):
    result = kvat("key=value")
    assert result.key == "key"
    assert result.value == "value"
    assert result.sep == "="
    assert result.orig == "key=value"
