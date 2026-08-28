
import pytest
from thefuck.types import Rule

def test_edge_case():
    rule = Rule(name=None, match=None, get_new_command=None, enabled_by_default=False, side_effect=lambda cmd, new_cmd: print('Side effect'), priority=1, requires_output=True)
    assert rule.name is None
    with pytest.raises(TypeError):
        assert rule.match(None) is False
