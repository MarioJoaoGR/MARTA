
import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.virtual.sysctl import VirtualSysctlDetectionMixin

class TestVirtualSysctlDetectionMixin:
    
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.mixin = VirtualSysctlDetectionMixin()
        self.mixin.module = MagicMock()
        self.mixin.sysctl_path = 'sysctl'  # Assuming sysctl is available and accessible
    
    def test_detect_virt_product_kvm(self):
        key = 'security.jail.jailed'
        expected_output = {
            'virtualization_type': 'kvm',
            'virtualization_role': 'guest',
            'virtualization_tech_guest': {'kvm'},
            'virtualization_tech_host': set()
        }
        
        self.mixin.module.run_command.return_value = (0, 'KVM', '')
        result = self.mixin.detect_virt_product(key)
        
        assert result == expected_output
    
    def test_detect_virt_product_vmware(self):
        key = 'vm.something'
        expected_output = {
            'virtualization_type': 'VMware',
            'virtualization_role': 'guest',
            'virtualization_tech_guest': {'VMware'},
            'virtualization_tech_host': set()
        }
        
        self.mixin.module.run_command.return_value = (0, 'VMware', '')
        result = self.mixin.detect_virt_product(key)
        
        assert result == expected_output
    
    def test_detect_virt_product_virtualbox(self):
        key = 'vbox.something'
        expected_output = {
            'virtualization_type': 'virtualbox',
            'virtualization_role': 'guest',
            'virtualization_tech_guest': {'virtualbox'},
            'virtualization_tech_host': set()
        }
        
        self.mixin.module.run_command.return_value = (0, 'VirtualBox', '')
        result = self.mixin.detect_virt_product(key)
        
        assert result == expected_output
    
    def test_detect_virt_product_xen(self):
        key = 'xen.something'
        expected_output = {
            'virtualization_type': 'xen',
            'virtualization_role': 'guest',
            'virtualization_tech_guest': {'xen'},
            'virtualization_tech_host': set()
        }
        
        self.mixin.module.run_command.return_value = (0, 'XenPVH', '')
        result = self.mixin.detect_virt_product(key)
        
        assert result == expected_output
    
    def test_detect_virt_product_hyperv(self):
        key = 'hyperv.something'
        expected_output = {
            'virtualization_type': 'Hyper-V',
            'virtualization_role': 'guest',
            'virtualization_tech_guest': {'Hyper-V'},
            'virtualization_tech_host': set()
        }
        
        self.mixin.module.run_command.return_value = (0, 'Hyper-V', '')
        result = self.mixin.detect_virt_product(key)
        
        assert result == expected_output
    
    def test_detect_virt_product_parallels(self):
        key = 'parallels.something'
        expected_output = {
            'virtualization_type': 'parallels',
            'virtualization_role': 'guest',
            'virtualization_tech_guest': {'parallels'},
            'virtualization_tech_host': set()
        }
        
        self.mixin.module.run_command.return_value = (0, 'Parallels', '')
        result = self.mixin.detect_virt_product(key)
        
        assert result == expected_output
    
    def test_detect_virt_product_rhev(self):
        key = 'rhevm.something'
        expected_output = {
            'virtualization_type': 'RHEV',
            'virtualization_role': 'guest',
            'virtualization_tech_guest': {'RHEV'},
            'virtualization_tech_host': set()
        }
        
        self.mixin.module.run_command.return_value = (0, 'RHEV Hypervisor', '')
        result = self.mixin.detect_virt_product(key)
        
        assert result == expected_output
    
    def test_detect_virt_product_jails(self):
        key = 'security.jail.jailed'
        expected_output = {
            'virtualization_type': 'jails',
            'virtualization_role': 'guest',
            'virtualization_tech_guest': {'jails'},
            'virtualization_tech_host': set()
        }
        
        self.mixin.module.run_command.return_value = (0, '1', '')
        result = self.mixin.detect_virt_product(key)
        
        assert result == expected_output
