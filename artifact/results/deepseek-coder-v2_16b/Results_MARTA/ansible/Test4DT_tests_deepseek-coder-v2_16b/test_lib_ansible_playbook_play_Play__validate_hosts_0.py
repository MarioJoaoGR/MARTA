
import pytest
from ansible.playbook.play import Play
from ansible.errors import AnsibleParserError
from typing import List, Union

# Helper function to create a minimal valid play configuration
def create_valid_play():
    return Play()

# Scenario 1: test_valid_hosts
def test_valid_hosts():
    play = create_valid_play()
    play._hosts = ['localhost']
    assert play._hosts == ['localhost'], "Expected hosts list to be ['localhost']"

# Scenario 2: test_empty_hosts
def test_empty_hosts():
    play = create_valid_play()
    with pytest.raises(AnsibleParserError) as excinfo:
        play._hosts = []
    assert str(excinfo.value) == "Hosts list cannot be empty. Please check your playbook", "Expected error for empty hosts list"

# Scenario 3: test_invalid_host_value
def test_invalid_host_value():
    play = create_valid_play()
    with pytest.raises(AnsibleParserError) as excinfo:
        play._hosts = [123]  # Invalid type (int)
    assert str(excinfo.value) == "Hosts list contains an invalid host value: '123'", "Expected error for invalid host value"
