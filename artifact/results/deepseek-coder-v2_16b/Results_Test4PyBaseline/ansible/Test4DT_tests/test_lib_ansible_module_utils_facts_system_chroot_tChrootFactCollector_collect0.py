# Module: ansible.module_utils.facts.system.chroot
import pytest
from ansible.module_utils.facts.system.chroot import ChrootFactCollector

# Mock the is_chroot function for testing purposes
def mock_is_chroot(*args, **kwargs):
    return False  # Default to not being a chroot environment in tests

# Monkey patch the is_chroot function during test execution
ChrootFactCollector.is_chroot = mock_is_chroot

@pytest.fixture
def collector():
    return ChrootFactCollector()

def test_default_initialization_and_collection(collector):
    result = collector.collect()
    assert 'is_chroot' in result, "Expected the result to contain 'is_chroot'"
    assert result['is_chroot'] == mock_is_chroot(), "Expected the default is_chroot value"

def test_using_with_mock_module(collector):
    class MockModule:
        def get_bin_path(self, binary_name, opt_dirs=None):
            if binary_name == 'facter':
                return '/usr/local/bin/facter'  # Replace with actual path if necessary
            elif binary_name == 'cfacter':
                return '/opt/puppetlabs/bin/cfacter'  # Replace with actual path if necessary

    module = MockModule()
    result = collector.collect(module=module)
    assert 'is_chroot' in result, "Expected the result to contain 'is_chroot'"
    assert result['is_chroot'] == mock_is_chroot(), "Expected the default is_chroot value"

def test_collecting_facts_with_custom_module(collector):
    class SomeModule:
        def params(self):
            return {'fact_path': '/some/custom/path'}  # Replace with actual path or parameters if necessary

    module = SomeModule()
    result = collector.collect(module=module)
    assert 'is_chroot' in result, "Expected the result to contain 'is_chroot'"
    assert result['is_chroot'] == mock_is_chroot(), "Expected the default is_chroot value"
