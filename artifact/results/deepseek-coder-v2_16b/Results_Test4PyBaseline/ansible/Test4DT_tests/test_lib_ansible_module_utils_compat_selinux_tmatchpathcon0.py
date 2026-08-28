
# Module: ansible.module_utils.compat.selinux
import pytest
from ansible.module_utils.compat.selinux import matchpathcon
try:
    import selinux
except ImportError:
    pytest.skip("selinux module not available", allow_module_level=True)

# Test cases for the matchpathcon function
def test_matchpathcon_basic():
    result = matchpathcon('/var/log/messages', selinux.MODE_READ)
    assert isinstance(result, list), "Expected a list as return type"
    assert len(result) == 2, "Expected a list with two elements"
    assert isinstance(result[0], int), "First element should be an integer (return code)"
    assert isinstance(result[1], str), "Second element should be a string (SELinux context)"

def test_matchpathcon_combination():
    result = matchpathcon('/var/log/messages', selinux.MODE_READ | selinux.MODE_WRITE)
    assert isinstance(result, list), "Expected a list as return type"
    assert len(result) == 2, "Expected a list with two elements"
    assert isinstance(result[0], int), "First element should be an integer (return code)"
    assert isinstance(result[1], str), "Second element should be a string (SELinux context)"

def test_matchpathcon_multiple():
    result = matchpathcon('/var/log/messages', selinux.MODE_READ | selinux.MODE_WRITE | selinux.MODE_EXEC | selinux.MODE_TRAVERSE)
    assert isinstance(result, list), "Expected a list as return type"
    assert len(result) == 2, "Expected a list with two elements"
    assert isinstance(result[0], int), "First element should be an integer (return code)"
    assert isinstance(result[1], str), "Second element should be a string (SELinux context)"
