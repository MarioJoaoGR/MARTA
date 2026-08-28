
import pytest
from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector

class MockModule:
    def __init__(self, get_bin_path=None):
        self._get_bin_path = get_bin_path if get_bin_path else lambda x: None
    
    def get_bin_path(self, bin_name):
        return self._get_bin_path(bin_name)

@pytest.fixture
def mock_module():
    return MockModule()


def test_is_systemd_managed_offline_no_systemctl(mock_module):
    mock_module = MockModule(get_bin_path=lambda x: None)
    service_mgr = ServiceMgrFactCollector()
    result = service_mgr.is_systemd_managed_offline(mock_module)
    assert result == False

def test_is_systemd_managed_offline_no_init_symlink(mock_module):
    mock_module = MockModule(get_bin_path=lambda x: 'systemctl' if x == 'systemctl' else None)
    service_mgr = ServiceMgrFactCollector()
    result = service_mgr.is_systemd_managed_offline(mock_module)
    assert result == False
