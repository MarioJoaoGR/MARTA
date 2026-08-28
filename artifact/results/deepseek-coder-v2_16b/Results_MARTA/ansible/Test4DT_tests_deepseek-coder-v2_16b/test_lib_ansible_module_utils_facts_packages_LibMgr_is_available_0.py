
import pytest
from ansible.module_utils.facts.packages import LibMgr


def test_invalid_input():
    with pytest.raises(TypeError):
        lib_mgr = LibMgr()