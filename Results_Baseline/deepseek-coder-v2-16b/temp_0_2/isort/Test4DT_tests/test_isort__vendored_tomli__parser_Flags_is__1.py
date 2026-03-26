
import pytest

from isort._vendored.tomli._parser import Flags


# Test initialization of the Flags class
def test_initialization():
    flags = Flags()
    assert hasattr(flags, '_flags')
    assert isinstance(flags._flags, dict)