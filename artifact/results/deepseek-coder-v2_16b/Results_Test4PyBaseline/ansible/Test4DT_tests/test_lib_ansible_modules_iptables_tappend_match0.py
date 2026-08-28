# Module: ansible.modules.iptables
import pytest
from ansible.modules.iptables import append_match

# Test case 1: When param is True, the match should be appended to the rule list
def test_append_match_with_truthy_param():
    rule = ['-c', 'some_command']
    append_match(rule, True, 'some_option')
    assert rule == ['-c', 'some_command', '-m', 'some_option']

# Test case 2: When param is False, the rule list should remain unchanged
def test_append_match_with_falsy_param():
    rule = []
    append_match(rule, False, 'another_option')
    assert rule == []

# Test case 3: When param is truthy (non-empty string), the match should be appended to the rule list
def test_append_match_with_truthy_string_param():
    rule = ['-c', 'some_command']
    append_match(rule, 'some_value', 'some_option')
    assert rule == ['-c', 'some_command', '-m', 'some_option']

# Test case 4: When param is falsy (empty string), the match should not be appended to the rule list
def test_append_match_with_falsy_string_param():
    rule = ['-c', 'some_command']
    append_match(rule, '', 'some_option')
    assert rule == ['-c', 'some_command']
