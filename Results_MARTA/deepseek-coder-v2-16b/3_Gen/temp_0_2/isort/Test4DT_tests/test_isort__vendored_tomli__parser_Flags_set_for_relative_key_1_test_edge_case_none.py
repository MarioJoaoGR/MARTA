
import pytest
from isort._vendored.tomli._parser import Flags, Key

def test_edge_case_none():
    flags = Flags()
    with pytest.raises(TypeError):
        flags.set_for_relative_key(Key("a"), Key("b"), 0)
