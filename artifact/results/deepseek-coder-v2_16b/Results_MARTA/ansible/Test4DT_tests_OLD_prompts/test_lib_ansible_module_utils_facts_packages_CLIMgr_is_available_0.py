
import pytest
from ansible.module_utils.facts.packages import CLIMgr

# Test case for when CLI is not set
def test_is_available_when_cli_not_set():
    with pytest.raises(TypeError):
        cli_mgr = CLIMgr()
