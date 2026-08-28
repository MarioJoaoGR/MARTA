
import pytest
from ansible.playbook.included_file import IncludedFile

# Test scenarios for IncludedFile class

def test_valid_inputs():
    filename = "example_file.txt"
    args = {"arg1": "value1"}
    vars = {"var1": "value1"}
    task = "task1"
    is_role = False
    
    included_file = IncludedFile(filename, args, vars, task, is_role)
    
    assert included_file._filename == filename
    assert included_file._args == args
    assert included_file._vars == vars
    assert included_file._task == task
    assert included_file._is_role == is_role

def test_edge_cases():
    # Test with None
    with pytest.raises(TypeError):
        IncludedFile(None, {"arg1": "value1"}, {"var1": "value1"}, "task1")
    
    # Test with empty lists
    included_file = IncludedFile("", {}, {}, "")
    assert included_file._filename == ""
    assert included_file._args == {}
    assert included_file._vars == {}
    assert included_file._task == ""
    assert not included_file._is_role

def test_invalid_inputs():
    with pytest.raises(TypeError):
        IncludedFile()  # Missing required arguments
