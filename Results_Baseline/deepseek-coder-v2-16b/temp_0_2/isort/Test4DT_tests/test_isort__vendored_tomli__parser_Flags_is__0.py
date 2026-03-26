# Module: isort._vendored.tomli._parser
import pytest

from isort._vendored.tomli._parser import Flags


# Test initialization of the Flags class
def test_initialization():
    flags = Flags()
    assert hasattr(flags, '_flags')
    assert isinstance(flags._flags, dict)
    assert len(flags._flags) == 0

# Test setting a flag recursively and checking if it is set
def test_set_for_relative_key():
    flags = Flags()
    flags.set_for_relative_key(["a", "b"], ["c"], Flags.EXPLICIT_NEST)
    assert flags.is_(["a", "b", "c"], Flags.EXPLICIT_NEST) == True

# Test setting a flag for a specific key without recursion and checking if it is set
def test_set_without_recursion():
    flags = Flags()
    flags.set(["a", "b", "c"], Flags.EXPLICIT_NEST, recursive=False)
    assert flags.is_(["a", "b", "c"], Flags.EXPLICIT_NEST) == True

# Test checking if a flag is not set for an invalid key path
def test_is_invalid_key():
    flags = Flags()
    assert flags.is_(["nonexistent", "path"], Flags.EXPLICIT_NEST) == False

# Test unsetting all flags for a key and checking if the flag is not set after unsetting
def test_unset_all():
    flags = Flags()
    flags.set_for_relative_key(["a", "b"], ["c"], Flags.EXPLICIT_NEST)
    assert flags.is_(["a", "b", "c"], Flags.EXPLICIT_NEST) == True
    flags.unset_all(["a", "b"])
    assert flags.is_(["a", "b", "c"], Flags.EXPLICIT_NEST) == False

# Test checking if a flag is set for an empty key path (should return False)
def test_is_empty_key():
    flags = Flags()
    assert flags.is_([], Flags.EXPLICIT_NEST) == False
