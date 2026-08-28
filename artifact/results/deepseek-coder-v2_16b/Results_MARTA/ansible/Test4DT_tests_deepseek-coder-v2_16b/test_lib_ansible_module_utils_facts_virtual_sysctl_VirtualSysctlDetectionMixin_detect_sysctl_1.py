
import pytest
from ansible.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin

def test_detect_sysctl_with_valid_module():
    class MockModule:
        def get_bin_path(self, bin_name):
            return "/usr/sbin/sysctl"
    
    instance = VirtualSysctlDetectionMixin()
    instance.module = MockModule()
    instance.detect_sysctl()
    assert instance.sysctl_path == "/usr/sbin/sysctl"
