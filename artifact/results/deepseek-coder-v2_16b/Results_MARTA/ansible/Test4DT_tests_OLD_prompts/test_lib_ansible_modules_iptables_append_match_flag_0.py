
import pytest
from ansible.modules.iptables import append_match_flag

def test_append_match_flag_with_match():
    rule = []
    append_match_flag(rule, 'match', 'ALLOW', False)
    assert rule == ['ALLOW']

def test_append_match_flag_with_negate_and_negatable():
    rule = ['ALLOW']
    append_match_flag(rule, 'negate', 'ALLOW', True)
    assert rule == ['ALLOW', '!', 'ALLOW']
