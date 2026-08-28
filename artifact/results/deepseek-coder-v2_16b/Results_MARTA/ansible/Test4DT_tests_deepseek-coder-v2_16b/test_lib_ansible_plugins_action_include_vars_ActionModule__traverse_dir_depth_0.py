
import pytest
from ansible.plugins.action import include_vars
from pathlib import Path

# Assuming we have an instance of ActionModule named 'am' with a source_dir attribute set.
@pytest.fixture(scope="module")
def am():
    return include_vars.ActionModule("valid_directory")



def test_invalid_inputs():
    # Test with a non-existent source_dir
    with pytest.raises(TypeError):
        include_vars.ActionModule("non_existent_directory")