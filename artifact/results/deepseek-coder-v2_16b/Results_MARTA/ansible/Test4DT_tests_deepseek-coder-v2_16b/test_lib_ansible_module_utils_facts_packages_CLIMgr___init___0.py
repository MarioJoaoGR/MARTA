
import pytest
from ansible.module_utils.facts.packages import CLIMgr

def test_missing_lines():
    with pytest.raises(TypeError):
        CLIMgr()

def test_invalid_input():
    with pytest.raises(TypeError):
        CLIMgr("invalid input")
