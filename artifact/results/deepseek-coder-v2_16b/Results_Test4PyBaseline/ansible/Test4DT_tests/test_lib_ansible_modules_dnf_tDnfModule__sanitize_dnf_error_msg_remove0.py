# Module: ansible.modules.dnf
import pytest
from ansible.module_utils.basic import AnsibleModule
import dnf

# Import the DnfModule class from its module
from ansible.modules.dnf import DnfModule

@pytest.fixture
def default_module():
    return AnsibleModule(argument_spec={})

@pytest.fixture
def custom_module():
    return AnsibleModule(argument_spec={'allowerasing': True, 'nobest': False})

class TestDnfModule:
    
    @pytest.mark.parametrize("module", [default_module(), custom_module()])
    def test_init_with_default_values(self, module):
        dnf_module = DnfModule(module=module)
        assert hasattr(dnf_module, 'lockfile')
        assert dnf_module.lockfile == "/var/cache/dnf/*_lock.pid"
        assert hasattr(dnf_module, 'pkg_mgr_name')
        assert dnf_module.pkg_mgr_name == "dnf"
        assert hasattr(dnf_module, 'with_modules')
        assert not dnf_module.with_modules
        assert hasattr(dnf_module, 'allowerasing')
        assert dnf_module.allowerasing is None  # Should be set from module params
        assert hasattr(dnf_module, 'nobest')
        assert dnf_module.nobest is None  # Should be set from module params

    @pytest.mark.parametrize("module", [custom_module()])
    def test_init_with_params(self, module):
        dnf_module = DnfModule(module=module)
        assert hasattr(dnf_module, 'lockfile')
        assert dnf_module.lockfile == "/var/cache/dnf/*_lock.pid"
        assert hasattr(dnf_module, 'pkg_mgr_name')
        assert dnf_module.pkg_mgr_name == "dnf"
        assert hasattr(dnf_module, 'with_modules')
        assert not dnf_module.with_modules
        assert hasattr(dnf_module, 'allowerasing')
        assert dnf_module.allowerasing == module.params['allowerasing']
        assert hasattr(dnf_module, 'nobest')
        assert dnf_module.nobest == module.params['nobest']

    def test_sanitize_dnf_error_msg_remove(self):
        dnf_module = DnfModule(module=AnsibleModule(argument_spec={}))
        # Test case where package is not installed
        result = dnf_module._sanitize_dnf_error_msg_remove('package', 'no package matched the request')
        assert not result[0]
        assert result[1] == "package is not installed"
        
        # Test case where there's a different error
        result = dnf_module._sanitize_dnf_error_msg_remove('package', 'Some other error message')
        assert result[0]
        assert result[1] == 'Some other error message'
