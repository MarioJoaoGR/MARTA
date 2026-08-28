
# Module: ansible.modules.iptables
from ansible.modules.iptables import append_match_flag

import pytest

# Test cases for append_match_flag function
def test_append_match_flag_with_match():
    rule = []
    append_match_flag(rule, 'match', 'ALLOWED', False)
    assert rule == ['ALLOWED']

def test_append_match_flag_with_negate_and_true_negatable():
    rule = []
    append_match_flag(rule, 'negate', 'ALLOWED', True)