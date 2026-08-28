
import pytest
from ansible.playbook.included_file import IncludedFile

# Test valid inputs
def test_valid_inputs():
    filename = "example_file.txt"
    args = {"arg1": "value1"}
    vars = {"var1": "value1"}
    task = "task1"
    is_role = True
    
    included_file = IncludedFile(filename, args, vars, task, is_role)
    
    assert included_file._filename == filename
    assert included_file._args == args
    assert included_file._vars == vars
    assert included_file._task == task
    assert included_file._is_role == is_role

# Test edge cases
def test_edge_cases():
    filename = None
    args = {}
    vars = []
    task = ""
    is_role = False
    
    included_file = IncludedFile(filename, args, vars, task, is_role)
    
    assert included_file._filename == filename
    assert included_file._args == args
    assert included_file._vars == vars
    assert included_file._task == task
    assert included_file._is_role == is_role

# Test invalid inputs
def test_invalid_inputs():
    with pytest.raises(TypeError):
        filename = 12345
        args = {"arg1": "value1", "arg2": None}
        vars = {"var1": "value1", "var2": []}
        task = "task1"
        is_role = True
        
        IncludedFile(filename, args, vars, task, is_role)
