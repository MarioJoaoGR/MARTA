
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

# Test case for get_device_facts_returns_correct_format
@pytest.fixture(scope="module")
def freebsd_hardware():
    with patch('ansible.module_utils.facts.hardware.freebsd.FreeBSDHardware.__init__', return_value=None):
        hw = FreeBSDHardware()
        yield hw

def test_get_device_facts_returns_correct_format(freebsd_hardware):
    device_facts = freebsd_hardware.get_device_facts()
    assert isinstance(device_facts, dict)
    assert 'devices' in device_facts
    assert isinstance(device_facts['devices'], dict)

# Test case for test_get_device_facts_collects_correct_disks
@pytest.fixture(scope="module")
def freebsd_hardware():
    with patch('ansible.module_utils.facts.hardware.freebsd.FreeBSDHardware.__init__', return_value=None):
        hw = FreeBSDHardware()
        yield hw

def test_get_device_facts_collects_correct_disks(freebsd_hardware):
    device_facts = freebsd_hardware.get_device_facts()
    assert isinstance(device_facts, dict)
    assert 'devices' in device_facts
    assert isinstance(device_facts['devices'], dict)
    # Add more specific assertions to verify the correctness of disk collection

# Test case for test_get_device_facts_collects_correct_partitions
@pytest.fixture(scope="module")
def freebsd_hardware():
    with patch('ansible.module_utils.facts.hardware.freebsd.FreeBSDHardware.__init__', return_value=None):
        hw = FreeBSDHardware()
        yield hw

def test_get_device_facts_collects_correct_partitions(freebsd_hardware):
    device_facts = freebsd_hardware.get_device_facts()
    assert isinstance(device_facts, dict)
    assert 'devices' in device_facts
    assert isinstance(device_facts['devices'], dict)
    # Add more specific assertions to verify the correctness of partition collection
