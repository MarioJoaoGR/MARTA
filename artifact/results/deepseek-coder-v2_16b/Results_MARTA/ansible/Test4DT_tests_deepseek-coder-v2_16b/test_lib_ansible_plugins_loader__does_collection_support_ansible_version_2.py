
import pytest
from ansible.plugins.loader import display
from packaging.specifiers import SpecifierSet
from packaging.version import Version

def _does_collection_support_ansible_version(requirement_string, ansible_version):
    if not requirement_string:
        return True

    if not SpecifierSet:
        display.warning('packaging Python module unavailable; unable to validate collection Ansible version requirements')
        return True

    ss = SpecifierSet(requirement_string)

    # ignore prerelease/postrelease/beta/dev flags for simplicity
    base_ansible_version = Version(ansible_version).base_version

    return ss.contains(base_ansible_version)

# Test 1: Collection supports specified Ansible version
def test_collection_supports_specified_ansible_version():
    result = _does_collection_support_ansible_version(">=2.9,<3.0", "2.10")
    assert result is True

# Test 2: Collection does not support specified Ansible version
def test_collection_does_not_support_specified_ansible_version():
    result = _does_collection_support_ansible_version(">=2.9,<3.0", "2.8")
    assert result is False

# Test 3: Collection supports unspecified Ansible version
def test_collection_supports_unspecified_ansible_version():
    result = _does_collection_support_ansible_version("", "2.10")
    assert result is True

# Test 4: Handling invalid requirement string
def test_invalid_requirement_string():
    with pytest.raises(Exception):
        _does_collection_support_ansible_version("invalid_requirement", "2.10")

# Test 5: Packaging module unavailable