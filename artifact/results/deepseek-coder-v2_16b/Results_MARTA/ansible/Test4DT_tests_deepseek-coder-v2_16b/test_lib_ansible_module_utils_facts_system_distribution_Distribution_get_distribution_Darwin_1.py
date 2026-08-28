
import pytest
from ansible.module_utils.facts.system.distribution import Distribution

@pytest.fixture(scope="function")
def module():
    # Create a mock AnsibleModule object for testing
    class MockAnsibleModule:
        def __init__(self):
            self.params = {}
        
        def run_command(self, command):
            if command == "/usr/bin/sw_vers -productVersion":
                return (0, "12.34.56\n", "")
            else:
                raise ValueError("Unknown command")
    
    module = MockAnsibleModule()
    return module

def test_get_distribution_Darwin(module):
    distro = Distribution(module)
    result = distro.get_distribution_Darwin()
    assert result == {'distribution': 'MacOSX', 'distribution_major_version': '12', 'distribution_version': '12.34.56'}
