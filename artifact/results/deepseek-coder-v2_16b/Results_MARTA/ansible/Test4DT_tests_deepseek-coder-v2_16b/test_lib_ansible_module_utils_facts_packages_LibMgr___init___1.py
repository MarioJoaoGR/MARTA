
import pytest
from ansible.module_utils.facts.packages import LibMgr


def test_invalid_input():
    # Attempt to create an instance of LibMgr without initializing it with a library
    with pytest.raises(TypeError):
        lib_mgr = LibMgr()