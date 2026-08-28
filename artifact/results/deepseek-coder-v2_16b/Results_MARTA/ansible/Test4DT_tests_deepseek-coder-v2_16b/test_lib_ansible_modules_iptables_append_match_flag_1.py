
import pytest
from ansible.modules.iptables import append_match_flag

# Test 1: Appending a match flag
def test_append_match_flag_with_match():
    rule = []
    append_match_flag(rule, 'match', 'ALLOW', False)
    assert rule == ['ALLOW']

# Test 2: Appending a negated flag where the flag can be negated
def test_append_match_flag_with_negate():
    rule = []
    append_match_flag(rule, 'negate', 'DENY', True)
    assert rule == ['!', 'DENY']

# Test 3: Appending a match flag where the flag cannot be negated (should not change the rule)
def test_append_match_flag_with_match_and_non_negatable():
    rule = []
    append_match_flag(rule, 'match', 'ALLOW', False)
    assert rule == ['ALLOW']

# Test 4: Appending a negated flag where the flag can be negated (should add negation)
def test_append_match_flag_with_negate_and_negatable():
    rule = []
    append_match_flag(rule, 'negate', 'ALLOW', True)
    assert rule == ['!', 'ALLOW']
