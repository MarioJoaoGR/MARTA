
import pytest
from ansible.plugins.become.su import BecomeModule

@pytest.fixture(scope="module")
def su_module():
    return BecomeModule()



def test_build_become_command_empty_cmd(su_module):
    cmd = ''
    result = su_module.build_become_command(cmd, True)
    assert result == ""