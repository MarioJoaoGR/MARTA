
import pytest
from ansible.inventory.group import Group
from ansible.inventory.helpers import get_group_vars

def test_get_group_vars_empty_groups():
    """Test when no groups are provided."""
    combined_vars = get_group_vars([])
    assert combined_vars == {}

def test_get_group_vars_none_input():
    """Test when the input is None."""
    with pytest.raises(TypeError):
        get_group_vars(None)

def test_get_group_vars_single_group():
    """Test when there's only one group in the list."""
    class Group:
        def __init__(self, depth, priority, name, vars_dict):
            self.depth = depth
            self.priority = priority
            self.name = name
            self.vars = vars_dict
        
        def get_vars(self):
            return self.vars
    
    groupA = Group(1, 1, 'groupA', {'varA': 'valueA'})
    combined_vars = get_group_vars([groupA])
    assert combined_vars == {'varA': 'valueA'}

def test_get_group_vars_multiple_groups():
    """Test when there are multiple groups with different variables."""
    class Group:
        def __init__(self, depth, priority, name, vars_dict):
            self.depth = depth
            self.priority = priority
            self.name = name
            self.vars = vars_dict
        
        def get_vars(self):
            return self.vars
    
    groupA = Group(1, 1, 'groupA', {'varA': 'valueA'})
    groupB = Group(2, 2, 'groupB', {'varB': 'valueB'})
    combined_vars = get_group_vars([groupA, groupB])
    assert combined_vars == {'varA': 'valueA', 'varB': 'valueB'}

def test_get_group_vars_duplicate_variables():
    """Test when multiple groups have variables with the same name."""
    class Group:
        def __init__(self, depth, priority, name, vars_dict):
            self.depth = depth
            self.priority = priority
            self.name = name
            self.vars = vars_dict
        
        def get_vars(self):
            return self.vars
    
    groupA = Group(1, 1, 'groupA', {'var': 'valueA'})
    groupB = Group(2, 2, 'groupB', {'var': 'valueB'})
    combined_vars = get_group_vars([groupA, groupB])
    assert combined_vars == {'var': 'valueB'}
