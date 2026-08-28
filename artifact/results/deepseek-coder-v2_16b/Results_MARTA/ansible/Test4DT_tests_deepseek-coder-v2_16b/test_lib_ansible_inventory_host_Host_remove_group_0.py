
import pytest
from ansible.inventory.host import Host

# Test valid input scenario
def test_valid_input():
    host = Host(name='exampleHost', port=22)
    group = "webservers"
    host.groups.append(group)  # Adding a predefined group for testing
    
    assert group in host.groups
    
    removed = host.remove_group(group)
    
    assert not removed
    assert group not in host.groups

# Test edge case scenario where the group to be removed is not in the host's groups
def test_edge_case():
    host = Host(name='exampleHost', port=22)
    non_existent_group = "non_existent_group"
    
    assert len(host.groups) == 0
    
    removed = host.remove_group(non_existent_group)
    
    assert not removed
    assert len(host.groups) == 0

# Test invalid input scenario with NoneType as argument
def test_invalid_input():
    host = Host(name='exampleHost', port=22)
    with pytest.raises(TypeError):
        host.remove_group(None)
