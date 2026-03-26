
from isort._vendored.tomli._parser import Flags
import pytest
from typing import Dict

def test_flags_init():
    flags = Flags()
    assert isinstance(flags._flags, dict), "Expected _flags to be a dictionary"
    assert flags._flags == {}, "Expected _flags to be an empty dictionary initially"
