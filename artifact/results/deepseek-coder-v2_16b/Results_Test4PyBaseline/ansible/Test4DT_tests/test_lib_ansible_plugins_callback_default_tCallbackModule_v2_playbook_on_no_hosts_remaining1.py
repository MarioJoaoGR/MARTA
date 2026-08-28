
import pytest
from ansible.plugins.callback import default

# Creating an instance of CallbackModule
@pytest.fixture
def callback_module():
    return default.CallbackModule()

# Test case to check the banner message when no hosts are left
def test_v2_playbook_on_no_hosts_remaining(capsys, callback_module):
    # Call the method to be tested
    callback_module.v2_playbook_on_no_hosts_remaining()
    
    # Capture stdout and check if the banner is displayed correctly
    captured = capsys.readouterr()
    assert "NO MORE HOSTS LEFT" in captured.out

# Test case to ensure no hosts remaining does not trigger the method when there are still hosts left
def test_v2_playbook_on_no_hosts_remaining_with_hosts(capsys, callback_module):
    # Mocking a scenario where there are still hosts left (for example, setting self._hosts to a non-empty list)
    callback_module._hosts = ['host1', 'host2']  # Assuming _hosts is an attribute that holds the list of hosts
    
    # Call the method to be tested
    callback_module.v2_playbook_on_no_hosts_remaining()
    
    # Capture stdout and check if no banner is displayed (or any other expected behavior)
    captured = capsys.readouterr()