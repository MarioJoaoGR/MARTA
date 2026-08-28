
import pytest
from ansible.playbook.included_file import IncludedFile

def test_valid_initialization():
    included_file = IncludedFile("example_file.txt", {"arg1": "value1"}, {"var1": "value1"}, "task1")
    assert included_file._filename == "example_file.txt"
    assert included_file._args == {"arg1": "value1"}
    assert included_file._vars == {"var1": "value1"}
    assert included_file._task == "task1"
    assert not included_file._is_role
    assert included_file._hosts == []

def test_add_host():
    included_file = IncludedFile("example_file.txt", {"arg1": "value1"}, {"var1": "value1"}, "task1")
    included_file.add_host('server1')
    assert included_file._hosts == ['server1']

def test_add_existing_host():
    included_file = IncludedFile("example_file.txt", {"arg1": "value1"}, {"var1": "value1"}, "task1")
    included_file.add_host('server1')
    with pytest.raises(ValueError):
        included_file.add_host('server1')
