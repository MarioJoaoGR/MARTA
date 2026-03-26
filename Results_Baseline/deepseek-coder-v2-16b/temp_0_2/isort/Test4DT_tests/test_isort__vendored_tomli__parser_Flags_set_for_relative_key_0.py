
import pytest

from isort._vendored.tomli._parser import Flags


# Test initialization of the Flags class
def test_initialization():
    flags = Flags()
    assert hasattr(flags, '_flags')
    assert isinstance(flags._flags, dict)
    assert len(flags._flags) == 0

# Test setting a flag recursively
def test_set_for_relative_key():
    flags = Flags()
    head_key = ["a", "b"]
    rel_key = ["c"]
    flag = Flags.EXPLICIT_NEST
    flags.set_for_relative_key(head_key, rel_key, flag)
    
    cont = flags._flags
    for k in head_key:
        assert k in cont
        cont = cont[k]["nested"]
    for k in rel_key:
        assert k in cont
        assert Flags.EXPLICIT_NEST in cont[k]["flags"]

# Test checking if a flag is set
def test_is_():
    flags = Flags()
    head_key = ["a", "b"]
    rel_key = ["c"]
    flag = Flags.EXPLICIT_NEST
    flags.set_for_relative_key(head_key, rel_key, flag)
    
    result = flags.is_(["a", "b", "c"], Flags.EXPLICIT_NEST)
    assert result is True

# Test unsetting all flags for a key
def test_unset_all():
    flags = Flags()
    head_key = ["a", "b"]
    rel_key = ["c"]
    flag = Flags.EXPLICIT_NEST
    flags.set_for_relative_key(head_key, rel_key, flag)
    