
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin

# Test class for the detect_virt_vendor method
class TestVirtualSysctlDetectionMixin:
    
    @patch('ansible.module_utils.facts.virtual.sysctl.VirtualSysctlDetectionMixin.detect_sysctl')
    def test_detect_virt_vendor_qemu(self, mock_detect_sysctl):
        # Mock the module object with run_command method returning QEMU output
        module_mock = MagicMock()
        module_mock.run_command.return_value = (0, 'QEMU\n', '')
        
        # Instantiate the class with the mocked module
        instance = VirtualSysctlDetectionMixin(module=module_mock)
        
        # Call the detect_virt_vendor method
        result = instance.detect_virt_vendor('kernel.vmx')
        
        # Assertions to check if the output is as expected
        assert 'virtualization_type' in result
        assert result['virtualization_type'] == 'kvm'
        assert 'virtualization_role' in result
        assert result['virtualization_role'] == 'guest'
        assert 'virtualization_tech_guest' in result
        assert result['virtualization_tech_guest'] == {'kvm'}
        assert 'virtualization_tech_host' in result
        assert result['virtualization_tech_host'] == set()
    
    @patch('ansible.module_utils.facts.virtual.sysctl.VirtualSysctlDetectionMixin.detect_sysctl')
    def test_detect_virt_vendor_openbsd(self, mock_detect_sysctl):
        # Mock the module object with run_command method returning OpenBSD output
        module_mock = MagicMock()
        module_mock.run_command.return_value = (0, 'OpenBSD\n', '')
        
        # Instantiate the class with the mocked module
        instance = VirtualSysctlDetectionMixin(module=module_mock)
        
        # Call the detect_virt_vendor method
        result = instance.detect_virt_vendor('kernel.vmx')
        
        # Assertions to check if the output is as expected
        assert 'virtualization_type' in result
        assert result['virtualization_type'] == 'vmm'
        assert 'virtualization_role' in result
        assert result['virtualization_role'] == 'guest'
        assert 'virtualization_tech_guest' in result
        assert result['virtualization_tech_guest'] == {'vmm'}
        assert 'virtualization_tech_host' in result
        assert result['virtualization_tech_host'] == set()
    
    @patch('ansible.module_utils.facts.virtual.sysctl.VirtualSysctlDetectionMixin.detect_sysctl')
    def test_detect_virt_vendor_unknown(self, mock_detect_sysctl):
        # Mock the module object with run_command method returning unknown output
        module_mock = MagicMock()
        module_mock.run_command.return_value = (0, 'Unknown\n', '')
        
        # Instantiate the class with the mocked module
        instance = VirtualSysctlDetectionMixin(module=module_mock)
        
        # Call the detect_virt_vendor method
        result = instance.detect_virt_vendor('kernel.vmx')
        
        # Assertions to check if the output is as expected
        assert 'virtualization_type' not in result
        assert 'virtualization_role' not in result
        assert 'virtualization_tech_guest' not in result
        assert 'virtualization_tech_host' not in result
    
    @patch('ansible.module_utils.facts.virtual.sysctl.VirtualSysctlDetectionMixin.detect_sysctl')
    def test_detect_virt_vendor_error(self, mock_detect_sysctl):
        # Mock the module object with run_command method returning error code
        module_mock = MagicMock()
        module_mock.run_command.return_value = (1, '', 'Error')
        
        # Instantiate the class with the mocked module
        instance = VirtualSysctlDetectionMixin(module=module_mock)
        
        # Call the detect_virt_vendor method
        result = instance.detect_virt_vendor('kernel.vmx')
        
        # Assertions to check if the output is as expected in case of error
        assert 'virtualization_type' not in result
        assert 'virtualization_role' not in result
        assert 'virtualization_tech_guest' not in result
        assert 'virtualization_tech_host' not in result

# Run the tests
if __name__ == '__main__':
    pytest.main()
