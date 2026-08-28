# Module: ansible.modules.iptables
# test_append_jump.py
from ansible.modules.iptables import append_jump

def test_append_jump_when_param_is_true():
    rule = []
    param = True
    jump = 'ACCEPT'
    append_jump(rule, param, jump)
    assert rule == ['-j', 'ACCEPT']

def test_not_append_jump_when_param_is_false():
    rule = []
    param = False
    jump = 'DROP'
    append_jump(rule, param, jump)
    assert rule == []

def test_append_jump_with_empty_rule():
    rule = []
    param = True
    jump = 'ACCEPT'
    append_jump(rule, param, jump)
    assert rule == ['-j', 'ACCEPT']

def test_not_modify_rule_when_param_is_false():
    rule = ['-A INPUT', '-p tcp', '--dport 80', '-j LOG']
    param = False
    jump = 'DROP'
    original_rule = rule.copy()
    append_jump(rule, param, jump)
    assert rule == original_rule
