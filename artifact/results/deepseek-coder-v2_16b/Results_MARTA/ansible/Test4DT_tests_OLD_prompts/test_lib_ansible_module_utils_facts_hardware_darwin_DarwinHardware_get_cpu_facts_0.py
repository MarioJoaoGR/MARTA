
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.hardware.darwin import DarwinHardware

@pytest.fixture(scope="module")
def darwin_hardware():
    with patch('ansible.module_utils.facts.hardware.darwin.DarwinHardware.__init__', return_value=None):
        return DarwinHardware()

def test_get_cpu_facts_intel(darwin_hardware):
    # Mocking sysctl for Intel processor
    darwin_hardware.sysctl = {
        'machdep.cpu.brand_string': 'Intel Core i7',
        'machdep.cpu.core_count': 4,
        'hw.physicalcpu': 4,
        'hw.logicalcpu': 8
    }
    
    cpu_facts = darwin_hardware.get_cpu_facts()
    assert cpu_facts['processor'] == 'Intel Core i7'
    assert cpu_facts['processor_cores'] == 4
    assert cpu_facts['processor_vcpus'] == 8
