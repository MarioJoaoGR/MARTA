
import pytest
from ansible.playbook.role_include import IncludeRole
from ansible.errors import AnsibleParserError

# Test valid inputs - happy path
def test_valid_inputs_happy_path():
    data = {'block': 'example', 'role': 'example_role', 'task_include': ['task1', 'task2']}
    include_role = IncludeRole(data=data, block='example', role='example_role', task_include=['task1', 'task2'])
    
    assert include_role._block == 'example'
    assert include_role._role == 'example_role'
    assert include_role._task_include == ['task1', 'task2']
    assert len(include_role._from_files) == 0
    assert include_role._parent_role is None
    assert include_role._role_name is None
    assert include_role._role_path is None

# Test edge cases
def test_edge_cases():
    include_role = IncludeRole()
    
    with pytest.raises(AnsibleParserError):
        IncludeRole(block=None, role=None, task_include=None)

# Test invalid inputs - error handling
def test_invalid_inputs_error_handling():
    data = {'block': None, 'role': None, 'task_include': None}
    
    with pytest.raises(AnsibleParserError):
        IncludeRole(data=data, block='example', role='example_role', task_include=['task1', 'task2'])
