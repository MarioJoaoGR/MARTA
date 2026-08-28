
import pytest
from ansible.vars.manager import VariableManager

# Assuming host_groups is defined somewhere in a module or fixture setup
host_groups = ['group1', 'group2']  # Example groups, replace with actual definition if needed

def test_valid_inputs():
    variable_manager = VariableManager()
    with pytest.raises(AttributeError):
        variable_manager.plugins_by_groups()
