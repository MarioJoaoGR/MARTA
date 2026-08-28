
import pytest
from ansible.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin

@pytest.fixture(scope="function")
def sysctl_mixin():
    return VirtualSysctlDetectionMixin()



def test_detect_virt_vendor_invalid_key(sysctl_mixin):
    with pytest.raises(AttributeError):
        sysctl_mixin.detect_virt_vendor(key="invalid.key")