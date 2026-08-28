
# Module: ansible.modules.apt_repository
import pytest
from unittest.mock import patch
import ansible.module_utils.basic as basic
try:
    from ubuntu_sources_list import UbuntuSourcesList
except ImportError:
    class UbuntuSourcesList:  # Mock implementation for testing purposes
        def __init__(self, module):
            self.codename = None
            self.add_ppa_signing_keys_callback = None

        @staticmethod
        def _expand_ppa(ppa):
            return ['http://ppa.launchpad.net/owner/ppa/ubuntu', 'owner', 'ppa']

        @property
        def repos_urls(self):
            return ['http://example.com']

# Mock the necessary modules and functions for testing
@patch('distro.codename', return_value='focal')
def test_ubuntu_sources_list_init_with_auto_detection(mock_codename):
    module = basic.AnsibleModule(argument_spec=dict(
        codename=dict(required=False, type='str'),
    ))
    ubuntu_sources = UbuntuSourcesList(module)
    assert ubuntu_sources.codename == 'focal'

@patch('distro.codename', return_value='bionic')
def test_ubuntu_sources_list_init_with_specified_codename(mock_codename):
    module = basic.AnsibleModule(argument_spec=dict(
        codename=dict(required=True, type='str'),  # Specified codename
    ))
    ubuntu_sources = UbuntuSourcesList(module)
    assert ubuntu_sources.codename == 'bionic'

def test_ubuntu_sources_list_init_with_custom_codename_and_callback():
    def add_ppa_signing_keys(owner, ppa):
        pass  # Your code to add PPA signing keys here

    module = basic.AnsibleModule(argument_spec=dict(
        codename=dict(required=True, type='str'),  # Specified codename
    ))
    ubuntu_sources = UbuntuSourcesList(module, add_ppa_signing_keys)
    assert isinstance(ubuntu_sources.add_ppa_signing_keys_callback, type(add_ppa_signing_keys))

def test_expand_ppa():
    module = basic.AnsibleModule(argument_spec=dict(
        codename=dict(required=True, type='str'),  # Specified codename
    ))
    ubuntu_sources = UbuntuSourcesList(module)
    ppa_source = ubuntu_sources._expand_ppa('ppa:owner/ppa')
    assert ppa_source[0].startswith('http://ppa.launchpad.net/owner/ppa/ubuntu')
    assert ppa_source[1] == 'owner'
    assert ppa_source[2] == 'ppa'

def test_repos_urls():
    module = basic.AnsibleModule(argument_spec=dict(
        codename=dict(required=True, type='str'),  # Specified codename
    ))
    ubuntu_sources = UbuntuSourcesList(module)
    with patch('ubuntu_sources_list.UbuntuSourcesList.repos_urls', return_value=['http://example.com']):
        assert ubuntu_sources.repos_urls() == ['http://example.com']
