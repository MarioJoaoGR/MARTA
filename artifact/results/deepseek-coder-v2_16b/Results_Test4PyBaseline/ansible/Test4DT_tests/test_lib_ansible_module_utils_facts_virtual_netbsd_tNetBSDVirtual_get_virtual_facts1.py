
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.virtual.netbsd import NetBSDVirtual

@patch('os.path.exists', return_value=True)
def test_get_virtual_facts_with_xen(_):
    module_mock = MagicMock()
    netbsd_system = NetBSDVirtual(module_mock)
    
    # Mock the detect_virt_product and detect_virt_vendor methods to return appropriate values
    with patch.multiple(NetBSDVirtual, detect_virt_product=MagicMock(), detect_virt_vendor=MagicMock()):
        netbsd_system.detect_virt_product = MagicMock(return_value={'virtualization_tech_guest': set(['xen']), 'virtualization_tech_host': set([])})
        netbsd_system.detect_virt_vendor = MagicMock(return_value={'virtualization_tech_guest': set([]), 'virtualization_tech_host': set(['vmware'])})
        
        virtual_info = netbsd_system.get_virtual_facts()
        
        assert virtual_info['virtualization_type'] == 'xen'
        assert virtual_info['virtualization_role'] == 'guest'
        assert virtual_info['virtualization_tech_guest'] == {'xen'}
        assert virtual_info['virtualization_tech_host'] == set(['vmware'])

@patch('os.path.exists', return_value=False)
def test_get_virtual_facts_without_xen(_):
    module_mock = MagicMock()
    netbsd_system = NetBSDVirtual(module_mock)
    
    # Mock the detect_virt_product and detect_virt_vendor methods to return appropriate values
    with patch.multiple(NetBSDVirtual, detect_virt_product=MagicMock(), detect_virt_vendor=MagicMock()):
        netbsd_system.detect_virt_product = MagicMock(return_value={'virtualization_tech_guest': set([]), 'virtualization_tech_host': set(['vmware'])})
        netbsd_system.detect_virt_vendor = MagicMock(return_value={'virtualization_tech_guest': set([]), 'virtualization_tech_host': set(['vmware'])})
        
        virtual_info = netbsd_system.get_virtual_facts()
        
        assert virtual_info['virtualization_type'] == ''
        assert virtual_info['virtualization_role'] == ''
        assert virtual_info['virtualization_tech_guest'] == set([])
        assert virtual_info['virtualization_tech_host'] == set(['vmware'])

def test_get_virtual_facts_with_empty_defaults():
    module_mock = MagicMock()
    netbsd_system = NetBSDVirtual(module_mock)
    
    # Mock the detect_virt_product and detect_virt_vendor methods to return appropriate values
    with patch.multiple(NetBSDVirtual, detect_virt_product=MagicMock(), detect_virt_vendor=MagicMock()):
        netbsd_system.detect_virt_product = MagicMock(return_value={'virtualization_tech_guest': set([]), 'virtualization_tech_host': set(['vmware'])})
        netbsd_system.detect_virt_vendor = MagicMock(return_value={'virtualization_tech_guest': set([]), 'virtualization_tech_host': set(['vmware'])})
        
        virtual_info = netbsd_system.get_virtual_facts()
        
        assert virtual_info['virtualization_type'] == ''
        assert virtual_info['virtualization_role'] == ''
        assert virtual_info['virtualization_tech_guest'] == set([])