
import pytest
from ansible.playbook.included_file import IncludedFile

# Test for valid initialization of IncludedFile with correct types
def test_valid_initialization():
    filename = "example_file.txt"
    args = {"arg1": "value1"}
    vars = {"var1": "value1"}
    task = "task1"
    
    included_file = IncludedFile(filename, args, vars, task)
    
    assert isinstance(included_file._filename, str), "Filename should be a string"
    assert isinstance(included_file._args, dict), "Args should be a dictionary"
    assert isinstance(included_file._vars, dict), "Vars should be a dictionary"
    assert isinstance(included_file._task, str), "Task should be a string"
    assert isinstance(included_file._hosts, list), "Hosts should be a list"
    assert included_file._is_role is False, "Is_role should default to False"

# Test for invalid initialization with incorrect filename type