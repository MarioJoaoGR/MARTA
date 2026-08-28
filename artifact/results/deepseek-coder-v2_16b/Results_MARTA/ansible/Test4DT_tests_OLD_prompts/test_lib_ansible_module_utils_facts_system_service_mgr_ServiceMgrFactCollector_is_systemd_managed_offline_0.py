
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector

class MyModule:
    def get_bin_path(self, cmd):
        if cmd == 'systemctl':
            return '/usr/bin/systemctl'

def test_valid_input():
    with patch('ansible.module_utils.facts.system.service_mgr.os.path.islink', return_value=True):
        with patch('ansible.module_utils.facts.system.service_mgr.os.readlink', return_value='/usr/lib/systemd/systemd'):
            service_mgr = ServiceMgrFactCollector()
            result = service_mgr.is_systemd_managed_offline(MyModule())
            assert result is True

def test_invalid_input():
    with patch('ansible.module_utils.facts.system.service_mgr.os.path.islink', return_value=False):
        service_mgr = ServiceMgrFactCollector()
        result = service_mgr.is_systemd_managed_offline(MyModule())
        assert result is False
