
import pytest

from isort._vendored.tomli._parser import Flags


def test_flags_initialization():
    flags = Flags()
    assert hasattr(flags, '_flags') and isinstance(flags._flags, dict), "Flags instance should have a _flags attribute of type dict"
    assert flags._flags == {}, "After initialization, the _flags dictionary should be empty"

def test_unset_all_existing_key():
    flags = Flags()
    flags._flags['a'] = {'nested': {}}
    flags.unset_all(['a'])