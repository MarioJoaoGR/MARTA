
import pytest
from ansible.module_utils.facts.hardware.netbsd import NetBSDHardware

class MockNetBSDHardware(NetBSDHardware):
    def __init__(self):
        self.sysctl = {
            'machdep.dmi.system-product': 'Test Product',
            'machdep.dmi.system-version': '1.0',
            'machdep.dmi.system-uuid': 'abc-def-ghi-jkl',
            'machdep.dmi.system-serial': '12345',
            'machdep.dmi.system-vendor': 'Test Vendor'
        }

@pytest.fixture(scope="module")
def netbsd_hardware():
    return MockNetBSDHardware()

def test_valid_case(netbsd_hardware):
    dmi_facts = netbsd_hardware.get_dmi_facts()
    assert dmi_facts['product_name'] == 'Test Product'
    assert dmi_facts['product_version'] == '1.0'
    assert dmi_facts['product_uuid'] == 'abc-def-ghi-jkl'
    assert dmi_facts['product_serial'] == '12345'
    assert dmi_facts['system_vendor'] == 'Test Vendor'

