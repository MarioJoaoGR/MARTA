
import pytest
from isort._vendored.tomli._parser import Flags

def test_unset_all():
    flags = Flags()
    flags._flags["a"] = {"nested": {}}
    flags._flags["a"]["nested"]["b"] = 1
    
    # Unset the flag at key ["a", "b"]
    flags.unset_all(["a", "b"])
    
    # Check if the flag has been removed
    assert "b" not in flags._flags["a"]["nested"]
