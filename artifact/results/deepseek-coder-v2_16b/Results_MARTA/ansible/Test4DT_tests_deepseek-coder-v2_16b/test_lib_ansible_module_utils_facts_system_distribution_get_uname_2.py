
import pytest
from ansible.module_utils.facts.system.distribution import get_uname


def test_invalid_module():
    class InvalidModule:
        pass
    
    mock_module = InvalidModule()
    
    with pytest.raises(AttributeError):
        get_uname(mock_module)