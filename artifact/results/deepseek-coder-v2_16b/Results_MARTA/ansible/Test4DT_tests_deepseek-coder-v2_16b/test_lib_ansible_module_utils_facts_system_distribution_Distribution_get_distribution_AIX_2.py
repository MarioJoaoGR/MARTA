
import pytest
from ansible.module_utils.facts.system.distribution import Distribution
import os

@pytest.fixture(scope="module")
def module():
    class MockModule:
        def __init__(self):
            self.params = {}
        
        def run_command(self, command):
            if command == "/usr/bin/oslevel":
                return (0, "12.34", "")  # Example output for oslevel
            else:
                raise ValueError("Unknown command")
    
    mock_module = MockModule()
    distro = Distribution(mock_module)
    return mock_module


def test_get_distribution_AIX_no_minor(module):
    class MockModuleNoMinor:
        def __init__(self):
            self.params = {}
        
        def run_command(self, command):
            if command == "/usr/bin/oslevel":
                return (0, "12", "")  # Example output for oslevel without minor version
            else:
                raise ValueError("Unknown command")
    
    mock_module_no_minor = MockModuleNoMinor()
    distro_no_minor = Distribution(mock_module_no_minor)
    dist_info = distro_no_minor.get_distribution_AIX()
    assert 'distribution_major_version' in dist_info
    assert dist_info['distribution_major_version'] == '12'
    assert 'distribution_version' in dist_info
    assert dist_info['distribution_version'] == '12'
    assert 'distribution_release' not in dist_info