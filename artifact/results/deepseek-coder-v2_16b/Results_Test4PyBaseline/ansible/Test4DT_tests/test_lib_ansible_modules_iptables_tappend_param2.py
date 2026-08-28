
import pytest
from ansible.modules.iptables import append_param

# Test case 3: Appending a single string parameter (non-list flag) with None value
def test_append_single_string_none():
    rule = []
    append_param(rule, None, '-e', False)
    assert rule == []

# Test case 4: Appending a list of parameters (non-list flag) with empty list
def test_append_list_parameters_empty():
    rule = []
    append_param(rule, [], '-f', True)
    assert rule == []

# Test case 5: Appending a single string parameter (non-list flag) with '!' prefix
def test_append_single_string_with_bang():
    rule = []
    append_param(rule, '!negated', '-e', False)
    assert rule == ['!', '-e', 'negated']

# Test case 6: Appending a single string parameter (non-list flag) without '!' prefix
def test_append_single_string_without_bang():
    rule = []
    append_param(rule, 'normal', '-e', False)
    assert rule == ['-e', 'normal']

# Test case 7: Appending a list of parameters (non-list flag) with multiple items
def test_append_list_parameters_multiple():
    rule = []
    append_param(rule, ['!negated1', 'normal1', '!negated2', 'normal2'], '-f', True)
    assert rule == ['!', '-f', 'negated1', '-f', 'normal1', '!', '-f', 'negated2', '-f', 'normal2']
