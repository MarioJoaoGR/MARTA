
import pytest
from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector
import os

class MockModule:
    def __init__(self, systemd_present=True):
        self.systemd_present = systemd_present
    
    def get_bin_path(self, command):
        if command == 'systemctl':
            return '/usr/bin/systemctl'
    
    def run_command(self):
        pass

@pytest.fixture
def create_service_mgr():
    return ServiceMgrFactCollector()

@pytest.fixture
def mock_module_systemd_present():
    return MockModule(systemd_present=True)

@pytest.fixture
def mock_module_no_systemd():
    return MockModule(systemd_present=False)


def test_invalid_systemd_absent(create_service_mgr, mock_module_no_systemd):
    result = create_service_mgr.is_systemd_managed(mock_module_no_systemd)
    assert result is False, "Expected systemd to be absent but got True"