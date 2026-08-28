
import pytest
from ansible.module_utils.facts.packages import CLIMgr


def test_direct_instantiation_and_is_available():
    with pytest.raises(TypeError):
        cli_mgr = CLIMgr()
