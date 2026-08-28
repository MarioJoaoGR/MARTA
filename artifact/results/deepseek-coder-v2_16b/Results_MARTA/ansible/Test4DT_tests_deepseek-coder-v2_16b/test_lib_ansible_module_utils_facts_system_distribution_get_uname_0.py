
import pytest
from ansible.module_utils.facts.system.distribution import get_uname

def test_get_uname_with_valid_module():
    # Create a mock module object with run_command method
    class MockModule:
        def run_command(self, command):
            return (0, "Linux", "")
    
    module = MockModule()
    result = get_uname(module)
    assert result == "Linux"

def test_get_uname_with_invalid_module():
    # Create a mock module object with run_command method that raises an AttributeError
    class InvalidMockModule:
        pass
    
    module = InvalidMockModule()
    with pytest.raises(AttributeError):
        get_uname(module)
