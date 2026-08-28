
import pytest
from ansible.plugins.become.su import BecomeModule

@pytest.fixture(scope="module")
def su_module():
    return BecomeModule()

# Test scenario 1: test_valid_input
def test_valid_input(su_module):
    cmd = 'ls -l'
    shell = True
    result = su_module.build_become_command(cmd, shell)
    assert result == "su -c ls -l admin"

# Test scenario 2: test_edge_case
def test_edge_case(su_module):
    cmd = ''
    shell = True
    result = su_module.build_become_command(cmd, shell)
    assert result == ""

# Test scenario 3: test_invalid_input
def test_invalid_input(su_module):
    cmd = None
    shell = True
    with pytest.raises(TypeError):
        su_module.build_become_command(cmd, shell)
