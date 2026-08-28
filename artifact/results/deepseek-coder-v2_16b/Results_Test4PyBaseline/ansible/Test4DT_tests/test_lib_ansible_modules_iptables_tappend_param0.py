
import pytest
from ansible.modules.iptables import append_param

# Test case 1: Appending a single string parameter (non-list flag)
def test_append_single_string():
    rule = []
    append_param(rule, 'example', '-e', False)
    assert rule == ['-e', 'example']

# Test case 2: Appending a list of parameters (non-list flag)
def test_append_list_parameters():
    rule = []
    append_param(rule, ['!negated', 'normal'], '-f', True)