# Module: ansible.plugins.callback.default
import pytest
from ansible.plugins.callback import default

# Creating an instance of CallbackModule
@pytest.fixture
def callback_module():
    return default.CallbackModule()

def test_v2_playbook_on_no_hosts_remaining(capsys, callback_module):
    # Call the method to be tested
    callback_module.v2_playbook_on_no_hosts_remaining()
    
    # Capture stdout and check if the banner is displayed correctly
    captured = capsys.readouterr()
    assert "NO MORE HOSTS LEFT" in captured.out
