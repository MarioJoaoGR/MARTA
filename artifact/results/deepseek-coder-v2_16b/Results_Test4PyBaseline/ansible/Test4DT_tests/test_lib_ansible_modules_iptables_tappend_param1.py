
import pytest
from ansible.modules.iptables import append_param

# Test case 3: Appending a single string parameter (non-list flag) with different flags
def test_append_single_string_different_flags():
    rule = []
    append_param(rule, 'example', '-e', False)
    assert rule == ['-e', 'example']
    
    rule = []
    append_param(rule, 'test', '-t', False)
    assert rule == ['-t', 'test']
    
    rule = []
    append_param(rule, 'value', '-v', False)
    assert rule == ['-v', 'value']

# Test case 4: Appending a list of parameters (non-list flag) with different flags
def test_append_list_parameters_different_flags():
    rule = []
    append_param(rule, ['!negated', 'normal'], '-f', True)
    assert rule == ['!', '-f', 'negated', '-f', 'normal']
    
    rule = []
    append_param(rule, ['-a', '-b'], '-j', True)
    assert rule == ['-j', '-a', '-j', '-b']
    
    rule = []
    append_param(rule, ['--option1', '--option2'], '-o', True)
    assert rule == ['-o', '--option1', '-o', '--option2']

# Test case 5: Handling None as a parameter (non-list flag)
def test_handle_none_parameter():
    rule = []
    append_param(rule, None, '-e', False)