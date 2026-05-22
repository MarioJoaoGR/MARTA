
import pytest
from httpie.compat import find_entry_points
from unittest.mock import patch, MagicMock
from importlib_metadata import EntryPoints

def test_invalid_inputs():
    class NonEntryPoints:
        pass
    
    ep = NonEntryPoints()
    
    with pytest.raises(AttributeError):
        find_entry_points(ep, 'mygroup')
