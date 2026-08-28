
import pytest
from ansible.modules.iptables import append_match

# Test case 5: When param is None (NoneType), the match should not be appended to the rule list
def test_append_match_with_none_param():
    rule = ['-c', 'some_command']
    append_match(rule, None, 'some_option')
    assert rule == ['-c', 'some_command'], f"Expected: [{'-c', 'some_command'}], Actual: {rule}"

# Test case 6: When param is an integer (truthy), the match should be appended to the rule list
def test_append_match_with_truthy_int_param():
    rule = ['-c', 'some_command']
    append_match(rule, 1, 'some_option')
    assert rule == ['-c', 'some_command', '-m', 'some_option'], f"Expected: [{'-c', 'some_command', '-m', 'some_option'}], Actual: {rule}"

# Test case 7: When param is zero (0, which is truthy in Python), the match should be appended to the rule list
def test_append_match_with_truthy_zero_param():
    rule = ['-c', 'some_command']
    append_match(rule, 0, 'some_option')