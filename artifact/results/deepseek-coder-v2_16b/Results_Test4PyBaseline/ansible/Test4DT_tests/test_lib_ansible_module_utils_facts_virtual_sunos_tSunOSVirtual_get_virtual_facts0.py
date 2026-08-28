
# Module: ansible.module_utils.facts.virtual.sunos
import pytest
from unittest.mock import MagicMock
from your_module import SunOSVirtual  # pylint: disable=E0401

# Fixture to create a mocked module for testing
@pytest.fixture
def mock_module():
    mock_module = MagicMock()
    mock_module.get_bin_path = MagicMock(side_effect=['zonename', 'modinfo', 'smbios'])
    mock_module.run_command = MagicMock(side_effect=[
        (0, 'global', ''),  # zonename
        (0, 'VMware\nVirtualBox\nKVM', ''),  # modinfo
        (0, 'VMware\nParallels\nVirtualBox\nHVM domU\nKVM', '')  # smbios
    ])
    return mock_module

# Test fixture for SunOSVirtual instance with mocked module
@pytest.fixture
def sunos_instance(mock_module):
    sunos_instance = SunOSVirtual()
    sunos_instance.module = mock_module
    return sunos_instance

# Test case to check if the function returns a dictionary when called without errors
def test_get_virtual_facts_returns_dict(sunos_instance):
    virtual_facts = sunos_instance.get_virtual_facts()
    assert isinstance(virtual_facts, dict)

# Test case to check if the function correctly identifies a global zone as host technology
def test_get_virtual_facts_identifies_global_zone_as_host(sunos_instance):
    virtual_facts = sunos_instance.get_virtual_facts()
    assert 'zone' in virtual_facts['virtualization_tech_host']
    assert virtual_facts['container'] == 'zone'

# Test case to check if the function correctly identifies VMware as guest technology
def test_get_virtual_facts_identifies_vmware_as_guest(sunos_instance):
    virtual_facts = sunos_instance.get_virtual_facts()
    assert 'vmware' in virtual_facts['virtualization_tech_guest']
    assert virtual_facts['virtualization_type'] == 'vmware'
    assert virtual_facts['virtualization_role'] == 'guest'

# Test case to check if the function correctly identifies VirtualBox as guest technology
def test_get_virtual_facts_identifies_virtualbox_as_guest(sunos_instance):
    virtual_facts = sunos_instance.get_virtual_facts()
    assert 'virtualbox' in virtual_facts['virtualization_tech_guest']
    assert virtual_facts['virtualization_type'] == 'virtualbox'
    assert virtual_facts['virtualization_role'] == 'guest'

# Test case to check if the function correctly identifies KVM as guest technology
def test_get_virtual_facts_identifies_kvm_as_guest(sunos_instance):
    virtual_facts = sunos_instance.get_virtual_facts()
    assert 'kvm' in virtual_facts['virtualization_tech_guest']
    assert virtual_facts['virtualization_type'] == 'kvm'
    assert virtual_facts['virtualization_role'] == 'guest'

# Test case to check if the function handles cases where no virtualization is detected
def test_get_virtual_facts_handles_no_virtualization(sunos_instance):
    mock_module = MagicMock()
    mock_module.get_bin_path = MagicMock(side_effect=[None, None])
    sunos_instance.module = mock_module
    virtual_facts = sunos_instance.get_virtual_facts()
    assert isinstance(virtual_facts, dict)
    assert 'virtualization_tech_guest' not in virtual_facts
    assert 'virtualization_tech_host' not in virtual_facts
