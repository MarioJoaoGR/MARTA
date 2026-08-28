
import pytest
from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector
import os

@pytest.fixture(scope="module")
def service_mgr():
    return ServiceMgrFactCollector()


def test_is_systemd_managed_offline_false(service_mgr):
    class MockModule:
        def __init__(self, bin_path=None):
            self._bin_paths = {'systemctl': bin_path}
        
        def get_bin_path(self, name):
            return self._bin_paths.get(name)
    
    mock_module = MockModule(None)  # No 'systemctl' binary path provided
    os.system = lambda cmd: 0 if cmd == "test -e /sbin/init && readlink /sbin/init | grep systemd" else 1
    
    result = service_mgr.is_systemd_managed_offline(mock_module)
    assert result is False, f"Expected False but got {result}"