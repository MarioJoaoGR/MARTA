
import pytest
from ansible.modules.iptables import append_match

def test_valid_case():
    rule = []
    append_match(rule, [80, 443], 'multiport')
    assert rule == ['-A', 'INPUT', '-p', 'tcp', '--dports', '80,443']

def test_edge_case():
    rule = []
    append_match(rule, [], 'multiport')
    assert rule == []
    
    rule = []
    append_match(rule, None, 'multiport')
    assert rule == []

def test_error_case():
    rule = []
    with pytest.raises(ValueError) as e:
        append_match(rule, 'invalid', 123)
    assert str(e.value) == "Invalid input type for destination ports"
