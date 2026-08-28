
import pytest
from unittest.mock import patch, MagicMock
from ansible.inventory.helpers import get_group_vars, sort_groups, combine_vars

def test_get_group_vars_valid():
    class Group:
        def __init__(self, depth, priority, name, vars_dict):
            self.depth = depth
            self.priority = priority
            self.name = name
            self.vars = vars_dict
        
        def get_vars(self):
            return self.vars
    
    groups_list = [Group(1, 2, 'groupC', {'varA': 'valueA'}), Group(2, 1, 'groupA', {'varB': 'valueB'})]
    
    with patch('ansible.inventory.helpers.sort_groups', return_value=sorted(groups_list, key=lambda g: (g.depth, g.priority, g.name))):
        combined_vars = get_group_vars(groups_list)
        assert isinstance(combined_vars, dict), "Expected a dictionary"
        assert 'varA' in combined_vars and combined_vars['varA'] == 'valueA', "Expected varA to be present with correct value"
        assert 'varB' in combined_vars and combined_vars['varB'] == 'valueB', "Expected varB to be present with correct value"
