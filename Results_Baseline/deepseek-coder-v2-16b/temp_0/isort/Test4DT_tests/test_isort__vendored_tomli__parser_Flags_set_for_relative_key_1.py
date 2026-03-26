
import pytest

from isort._vendored.tomli._parser import Flags


# Test initialization of the Flags class
def test_init():
    flags = Flags()
    assert isinstance(flags._flags, dict)
    assert flags._flags == {}

# Test setting a flag in an empty nested structure
def test_set_for_relative_key_empty_nested():
    flags = Flags()
    head_key = ['namespace']
    rel_key = ['subnamespace', 'deeply', 'nested']
    flag = Flags.EXPLICIT_NEST
    flags.set_for_relative_key(head_key, rel_key, flag)